function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu( 'Bank Customer Churn' )
    .addItem( 'Get Prediction', 'PredictAll')
    .addToUi();
}

// Production Server
host_production = 'churn-bank-pred-dj.herokuapp.com'

// ----------------------------
// ----- Helper Function ------
// ----------------------------
// API Call
function ApiCall( data, endpoint ){
  var url = 'https://' + host_production + endpoint;
  var payload = JSON.stringify( data );

  var options = {'method': 'POST', 'contentType': 'application/json', 'payload': payload};

  Logger.log( url )
  Logger.log( options )

  var response = UrlFetchApp.fetch( url, options );

  // get response
  var rc = response.getResponseCode();
  var responseText = response.getContentText();

  if ( rc !== 200 ){
    Logger.log( 'Response (%s) %s', rc, responseText );
  }
  else{
    prediction = JSON.parse( responseText );
  }
  return prediction
};

// Bank Customer Churn Propensity Score Prediction
function PredictAll(){
  //google sheets parameters
  var ss = SpreadsheetApp.getActiveSheet();
  var titleColumns = ss.getRange( 'A1:N1' ).getValues()[0];
  var lastRow = ss.getLastRow();

  var data = ss.getRange( 'A2' + ':' + 'N' + lastRow ).getValues();

  // run over all rows
  for ( row in data ){
    var json = new Object();
    
    // run over all columns
    for( var j=0; j < titleColumns.length; j++ ){
      json[titleColumns[j]] = data[row][j];
    };

    // Json file to send
    var json_send = new Object();
    json_send['row_number'] = json['row_number']
    json_send['customer_id'] = json['customer_id']
    json_send['surname'] = json['surname']
    json_send['credit_score'] = json['credit_score']
    json_send['geography'] = json['geography']
    json_send['gender'] = json['gender']
    json_send['age'] =  json['age']
    json_send['tenure'] = json['tenure']
    json_send['balance'] = json['balance']
    json_send['num_of_products'] = json['num_of_products']
    json_send['has_cr_card'] = json['has_cr_card']
    json_send['is_active_member'] = json['is_active_member']
    json_send['estimated_salary'] = json['estimated_salary']
    json_send['exited'] = json['exited']

    // Propensity score
    pred = ApiCall( json_send, '/getpred' );

    // Send back to google sheets
    ss.getRange( Number( row ) + 2 , 15 ).setValue('')
    ss.getRange( Number( row ) + 2 , 15 ).setValue( pred[0]['prob_churn'] )
    
    var planilha = SpreadsheetApp.getActiveSpreadsheet();
    var folha = planilha.getSheets()[0];
    var intervalo = folha.getRange('A2:O36');
    intervalo.sort([{column:15, ascending:false}]);
    Logger.log( pred[0]['prob_churn'] )
    Logger.log( row )
  };
};

