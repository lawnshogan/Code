nlapiLogExecution("audit","FLOStart",new Date().getTime());
//add comment

function bodySearch(request, response){

try
{
   var haAtlasNumber= request.getParameter('atlas');  // '100777';
    //

    var arrSearchFilters = new Array();
    arrSearchFilters[0] = new nlobjSearchFilter('mainline', null, 'is', 'T');
    arrSearchFilters[1] = new nlobjSearchFilter('tranid', null , 'is', haAtlasNumber);

    var arrSearchColumns = new Array();
    arrSearchColumns[0] = new nlobjSearchColumn('number',null,'group');
    arrSearchColumns[1] = new nlobjSearchColumn('entity',null,'group');
    arrSearchColumns[2] = new nlobjSearchColumn('internalid',null,'group');
    arrSearchColumns[3] = new nlobjSearchColumn('startdate',null,'group');
    arrSearchColumns[4] = new nlobjSearchColumn('enddate',null,'group');
    arrSearchColumns[5] = new nlobjSearchColumn('custbody_hein_lease_type',null,'group');
    arrSearchColumns[6] = new nlobjSearchColumn('location',null,'group');
    arrSearchColumns[7] = new nlobjSearchColumn('custbody_hein_legacy_lease',null,'group');
    arrSearchColumns[8] = new nlobjSearchColumn('custbody_hein_lease_subtype',null,'group');
    arrSearchColumns[9] = new nlobjSearchColumn('custbody_hein_lease_status',null,'group');
 

    var arrSearchResults = nlapiSearchRecord('salesorder', null, arrSearchFilters, arrSearchColumns);

    var htmlBody = '<body>';
 htmlBody += '<table class="tableHein" style="border-collapse: separate; border-spacing: 20px;">';

if (arrSearchResults != null && arrSearchResults.length > 0)
{

// Header
 htmlBody += '<tr>';
 htmlBody += ' <td> Number </td>';
 htmlBody += ' <td> Legacy Lease Number </td>';
 htmlBody += ' <td> Name </td>';
 htmlBody += ' <td> Start Date</td>';
 htmlBody += ' <td> End Date </td>';
 htmlBody += ' <td> Lease Type </td>';
 htmlBody += ' <td> Lease Subtype </td>';
 htmlBody += ' <td> District </td>';
 htmlBody += ' <td> Lease Status </td>';
 htmlBody += '</tr>';
 htmlBody += '<p><br>';
 
    for ( var i in arrSearchResults) {
        var searchResult = arrSearchResults[i];

        var haLeaseNum = searchResult.getValue('number',null,'group');
        var haCustName = searchResult.getText('entity',null,'group');
        var haStartDate = searchResult.getValue('startdate',null,'group');
        var haEndDate = searchResult.getValue('enddate',null,'group');
        var haInternalID = searchResult.getValue('internalid',null,'group');
        var haLeaseType = searchResult.getText('custbody_hein_lease_type',null,'group');
        var haDistrict = searchResult.getText('location',null,'group');
        var haLegacyLease = searchResult.getText('custbody_hein_legacy_lease',null,'group');
        var haLeaseSubtype = searchResult.getText('custbody_hein_lease_subtype',null,'group');
        var haLeaseStatus = searchResult.getText('custbody_hein_lease_status',null,'group');

var linkURL = nlapiResolveURL('RECORD','salesorder',haInternalID);

        htmlBody += '<tr>';
        htmlBody += ' <td><a href="'+ linkURL + '" target="_blank" >' + haLeaseNum  + '</td>';
        htmlBody += ' <td>' + haLegacyLease + '</td>';
		htmlBody += ' <td>' + haCustName + '</td>';
		htmlBody += ' <td>' + haStartDate + '</td>';
		htmlBody += ' <td>' + haEndDate + '</td>';
		htmlBody += ' <td>' + haLeaseType + '</td>';
        htmlBody += ' <td>' + haLeaseSubtype + '</td>';
        htmlBody += ' <td>' + haDistrict + '</td>';
        htmlBody += ' <td>' + haLeaseStatus + '</td>';
		htmlBody += '</tr>';
    }

}
else
{
 htmlBody += '<tr>';
 htmlBody += ' <td> No Results </td>';
 htmlBody += '</tr>';

}

 htmlBody += '</table>';
  htmlBody += '</body>';

    response.write(htmlBody);
 }
catch (e) {
            nlapiLogExecution("ERROR", "Body Search", "Error: " + e);
                         response.write(e);
        }

}



function itemSearch(request, response){

try
{
   var haAtlasNumber= request.getParameter('atlas');  // '100777';

    var arrSearchFilters = new Array();
    arrSearchFilters[0] = new nlobjSearchFilter('mainline', null, 'is', 'F');
    //arrSearchFilters[1] = new nlobjSearchFilter('isclosed', null, 'is', 'F');
    arrSearchFilters[1] = new nlobjSearchFilter('custcol_hein_print', null, 'is', 'T');
    arrSearchFilters[2] = new nlobjSearchFilter('tranid', null , 'is', haAtlasNumber);

    var arrSearchColumns = new Array();
    arrSearchColumns[0] = new nlobjSearchColumn('item',null,'group');
    arrSearchColumns[1] = new nlobjSearchColumn('custcol_hein_parcel_acres',null,'group');
	arrSearchColumns[2] = new nlobjSearchColumn('custcol_hein_asset_desc',null,'group');
    arrSearchColumns[3] = new nlobjSearchColumn('internalid',null,'group');
	

    var arrSearchResults = nlapiSearchRecord('transaction', null, arrSearchFilters, arrSearchColumns);


   


    var htmlBody = '<body>';
 htmlBody += '<table class="tableHein" style="border-collapse: separate; border-spacing: 20px;">';

if (arrSearchResults != null && arrSearchResults.length > 0)
{
// Header
 htmlBody += '<tr>';
 htmlBody += ' <td> Item </td>';
 htmlBody += ' <td> Acres </td>';
 htmlBody += ' <td> Legal Description </td>';
 htmlBody += '</tr>';
 htmlBody += '<p><br>';
 
    for ( var i in arrSearchResults) {
        var searchResult = arrSearchResults[i];

        var haItem = searchResult.getText('item',null,'group');
        var haAcres = searchResult.getValue('custcol_hein_parcel_acres',null,'group');
		var haLegalDescription = searchResult.getValue('custcol_hein_asset_desc',null,'group');
        var haInternalID = searchResult.getText('internalid',null,'group');

//var linkURL = nlapiResolveURL('RECORD','salesorder',haInternalID);

        htmlBody += '<tr>';
   //htmlBody += ' <td><a href="'+ linkURL +  '" target="_blank" >' + haLeaseNum + '</td>';
   htmlBody += ' <td>' + haItem + '</td>';
   htmlBody += ' <td>' + haAcres + '</td>';
   htmlBody += ' <td>' + haLegalDescription + '</td>';
   htmlBody += '</tr>';
    }
}
else
{
 htmlBody += '<tr>';
 htmlBody += ' <td> No Results </td>';
 htmlBody += '</tr>';

}

 htmlBody += '</table>';
  htmlBody += '</body>';

    response.write(htmlBody);
 }
catch (e) {
            nlapiLogExecution("ERROR", "Item Search", "Error: " + e);
                         response.write(e);
        }

}


function notesSearch(request, response){

try
{
   var haAtlasNumber= request.getParameter('atlas');  // '100777';

    var arrSearchFilters = new Array();
    //arrSearchFilters[0] = new nlobjSearchFilter('title', 'note', 'noneof', '@NONE@');
    arrSearchFilters[0] = new nlobjSearchFilter('tranid', 'transaction' , 'is', haAtlasNumber);
    
    var arrSearchColumns = new Array();
    arrSearchColumns[0] = new nlobjSearchColumn('title', null,'group');
    arrSearchColumns[1] = new nlobjSearchColumn('note', null,'group');
    arrSearchColumns[2] = new nlobjSearchColumn('author', null,'group');
    arrSearchColumns[3] = new nlobjSearchColumn('internalid', null ,'group');

    var arrSearchResults = nlapiSearchRecord('note', null, arrSearchFilters, arrSearchColumns);

   var htmlBody = '<body>';
 htmlBody += '<table class="tableHein" style="border-collapse: separate; border-spacing: 20px;">';

if (arrSearchResults != null && arrSearchResults.length > 0)
{
// Header
 htmlBody += '<tr>';
 htmlBody += ' <td> Title </td>';
 htmlBody += ' <td> Note Text </td>';
 htmlBody += ' <td> Author </td>';
 htmlBody += '</tr>';
 htmlBody += '<p><br>';
 
    for ( var i in arrSearchResults) {
        var searchResult = arrSearchResults[i];

        var haNoteTitle = searchResult.getValue('title', null,'group');
        var haNoteText = searchResult.getValue('note', null,'group');
        var haNoteAuthor = searchResult.getText('author', null,'group');
        var haInternalID = searchResult.getText('internalid',null,'group');

//var linkURL = nlapiResolveURL('RECORD','customrecord_hein_special_programs',haInternalID);

        htmlBody += '<tr>';
    //htmlBody += ' <td><a href="'+ linkURL + '" target="_blank" >' + haSPType   + '</td>';
   htmlBody += ' <td>' + haNoteTitle + '</td>';
   htmlBody += ' <td>' + haNoteText + '</td>';
   htmlBody += ' <td>' + haNoteAuthor + '</td>';
   htmlBody += '</tr>';
    }

}
else
{
 htmlBody += '<tr>';
 htmlBody += ' <td> No Results </td>';
 htmlBody += '</tr>';

}


 htmlBody += '</table>';
  htmlBody += '</body>';

    response.write(htmlBody);
 }
catch (e) {
            nlapiLogExecution("ERROR", "User Notes Search", "Error: " + e);
                         response.write(e);
        }

}

function bondSearch(request, response){
  try
{
   var haAtlasNumber= request.getParameter('atlas');  // '100777';
//ASK MARC- need to get the atlas number parameter and turn it into the internal ID of the lease. This group works if I put in the interal ID of a lease.
    var arrSearchFilters = new Array();
    arrSearchFilters[0] = new nlobjSearchFilter( 'tranid', 'custrecord_hein_related_lease',  'is', haAtlasNumber);
    arrSearchFilters[1] = new nlobjSearchFilter('custrecord_slb_bi_bond_or_insurance', null, 'is', 'Bond');
    
    var arrSearchColumns = new Array();
    arrSearchColumns[0] = new nlobjSearchColumn('custrecord_slb_bi_bond_type', null ,'group');
    arrSearchColumns[1] = new nlobjSearchColumn('custrecord_slb_bi_bond_classification', null ,'group');
    arrSearchColumns[2] = new nlobjSearchColumn('internalid', null ,'group');

    var arrSearchResults = nlapiSearchRecord('customrecord_hein_bonds_ins', null, arrSearchFilters, arrSearchColumns);

   var htmlBody = '<body>';
 htmlBody += '<table class="tableHein" style="border-collapse: separate; border-spacing: 20px;">';

if (arrSearchResults != null && arrSearchResults.length > 0)
{
// Header
 htmlBody += '<tr>';
 htmlBody += ' <td> Bond Type </td>';
 htmlBody += ' <td> Bond Classification </td>';
 //htmlBody += ' <td> Author </td>';
 htmlBody += '</tr>';
 htmlBody += '<p><br>';
 
    for ( var i in arrSearchResults) {
        var searchResult = arrSearchResults[i];

        var haBondType = searchResult.getText('custrecord_slb_bi_bond_type', null ,'group');
        var haBondClass = searchResult.getText('custrecord_slb_bi_bond_classification', null,'group');
        //var haNoteAuthor = searchResult.getText('author', 'customrecord_hein_bonds_ins','group');
        var haInternalID = searchResult.getText('internalid', null ,'group');

//var linkURL = nlapiResolveURL('RECORD','customrecord_hein_special_programs',haInternalID);

        htmlBody += '<tr>';
    //htmlBody += ' <td><a href="'+ linkURL + '" target="_blank" >' + haSPType   + '</td>';
   htmlBody += ' <td>' + haBondType + '</td>';
   htmlBody += ' <td>' + haBondClass + '</td>';
   //htmlBody += ' <td>' + haNoteAuthor + '</td>';
   htmlBody += '</tr>';
    }

}
else
{
 htmlBody += '<tr>';
 htmlBody += ' <td> No Results </td>';
 htmlBody += '</tr>';

}


 htmlBody += '</table>';
  htmlBody += '</body>';

    response.write(htmlBody);
 }
catch (e) {
            nlapiLogExecution("ERROR", "Bond Search", "Error: " + e);
                         response.write(e);
        }

}


function leaseactionsSearch(request, response){
  try
{
   var haAtlasNumber= request.getParameter('atlas');  // '100777';
    
    var arrSearchFilters = new Array();
    arrSearchFilters[0] = new nlobjSearchFilter('tranid', 'custrecord_slb_la_related_lease' , 'is', haAtlasNumber);
    
    var arrSearchColumns = new Array();
    arrSearchColumns[0] = new nlobjSearchColumn('custrecord_slb_la_lease_action_type', null ,'group');
    arrSearchColumns[1] = new nlobjSearchColumn('custrecord_slb_la_board_meeting_date', null ,'group');
    arrSearchColumns[2] = new nlobjSearchColumn('custrecord_slb_la_lease_approval_method', null ,'group');
    arrSearchColumns[3] = new nlobjSearchColumn('internalid', null ,'group');

    var arrSearchResults = nlapiSearchRecord('customrecord_slb_lease_actions', null, arrSearchFilters, arrSearchColumns);

   var htmlBody = '<body>';
 htmlBody += '<table class="tableHein" style="border-collapse: separate; border-spacing: 20px;">';

if (arrSearchResults != null && arrSearchResults.length > 0)
{
// Header
 htmlBody += '<tr>';
 htmlBody += ' <td> Lease Action Type </td>';
 htmlBody += ' <td> Board Meeting Date </td>';
 htmlBody += ' <td> Staff or Board Approval </td>';
 htmlBody += '</tr>';
 htmlBody += '<p><br>';
 
    for ( var i in arrSearchResults) {
        var searchResult = arrSearchResults[i];

        var haActionType = searchResult.getText('custrecord_slb_la_lease_action_type', null ,'group');
        var haMeetingDate = searchResult.getText('custrecord_slb_la_board_meeting_date', null,'group');
        var haApprovalMethod = searchResult.getText('custrecord_slb_la_lease_approval_method', null,'group');
        var haInternalID = searchResult.getText('internalid', null ,'group');

//var linkURL = nlapiResolveURL('RECORD','customrecord_hein_special_programs',haInternalID);

        htmlBody += '<tr>';
    //htmlBody += ' <td><a href="'+ linkURL + '" target="_blank" >' + haSPType   + '</td>';
   htmlBody += ' <td>' + haActionType + '</td>';
   htmlBody += ' <td>' + haMeetingDate + '</td>';
   htmlBody += ' <td>' + haApprovalMethod + '</td>';
   htmlBody += '</tr>';
    }

}
else
{
 htmlBody += '<tr>';
 htmlBody += ' <td> No Results </td>';
 htmlBody += '</tr>';

}


 htmlBody += '</table>';
  htmlBody += '</body>';

    response.write(htmlBody);
 }
catch (e) {
            nlapiLogExecution("ERROR", "Lease Actions Search", "Error: " + e);
                         response.write(e);
        }

}


/*function fileSearch(request, response){

try
{
   var haAtlasNumber= request.getParameter('atlas');  // '100777';
    //

    var arrSearchFilters = new Array();
    arrSearchFilters[0] = new nlobjSearchFilter('mainline', null, 'is', 'T');
    arrSearchFilters[1] = new nlobjSearchFilter('tranid', 'file' , 'is', haAtlasNumber);
    arrSearchFilters[2] = new nlobjSearchFilter('name', 'file' , 'noneof', '@NONE@');

    var arrSearchColumns = new Array();
    arrSearchColumns[0] = new nlobjSearchColumn('name', 'file' , null);
    //arrSearchColumns[1] = new nlobjSearchColumn('filetype','file','group');
    arrSearchColumns[1] = new nlobjSearchColumn('internalid','file' , null);  //this line can be the internal ID of the doc or the transaction depending on how it is needed
    //arrSearchColumns[3] = new nlobjSearchColumn('created','file','group');
   // arrSearchColumns[4] = new nlobjSearchColumn('modified','file','group');
    //arrSearchColumns[5] = new nlobjSearchColumn('folder','file','group');
    //arrSearchColumns[6] = new nlobjSearchColumn('documentsize','file','group');
   // arrSearchColumns[6].setSort(false);

 

    var arrSearchResults = nlapiSearchRecord('transaction', null, arrSearchFilters, arrSearchColumns);

    var htmlBody = '<body>';
 htmlBody += '<table class="tableHein" style="border-collapse: separate; border-spacing: 20px;">';

if (arrSearchResults != null && arrSearchResults.length > 0)
{

// Header
 htmlBody += '<tr>';
 htmlBody += ' <td> Name </td>';
 //htmlBody += ' <td> File Type </td>';
 //htmlBody += ' <td> Date Created</td>';
 //htmlBody += ' <td> Date Modified </td>';
 //htmlBody += ' <td> Folder </td>';
 //htmlBody += ' <td> Size (KB) </td>';
 htmlBody += '</tr>';
 htmlBody += '<p><br>';
 
    for ( var i in arrSearchResults) {
        var searchResult = arrSearchResults[i];

        var haFileName = searchResult.getText('name','file' ,'group');
        //var haFileType = searchResult.getText('filetype','file' ,'group');
        var haInternalID = searchResult.getValue('internalid','file' ,'group');
        //var haDateCreated = searchResult.getValue('created','file' ,'group');
        //var haDateModified = searchResult.getValue('modified','file' ,'group');    //this line can be the internal ID of the doc or the transaction depending on how it is needed
        //var haFolder = searchResult.getText('folder','file' ,'group');
        //var haDocSize = searchResult.getText('documentsize','file' ,'group');

//var linkURL = nlapiResolveURL('RECORD','salesorder',haInternalID);
        //LIST_MEDIAITEMFOLDER File Cabinet /app/common/media/mediaitemfolders.nl
        //use the href below and type in the beginning of the link followed by a URL var from above

        htmlBody += '<tr>';
        //htmlBody += ' <td><a href="'+ linkURL + '" target="_blank" >' + haLeaseNum  + '</td>';
		htmlBody += ' <td>' + haFileName + '</td>';
		//htmlBody += ' <td>' + haFileType + '</td>';
		//htmlBody += ' <td>' + haDateCreated + '</td>';
		//htmlBody += ' <td>' + haDateModified + '</td>';
        //htmlBody += ' <td>' + haFolder + '</td>';
       // htmlBody += ' <td>' + haDocSize + '</td>';
		htmlBody += '</tr>';
    }

}
else
{
 htmlBody += '<tr>';
 htmlBody += ' <td> No Results </td>';
 htmlBody += '</tr>';

}

 htmlBody += '</table>';
  htmlBody += '</body>';

    response.write(htmlBody);
 }
catch (e) {
            nlapiLogExecution("ERROR", "File Search", "Error: " + e);
                         response.write(e);
        }

}
*/

function inspectionSearch(request, response){

try
{
    var haAtlasNumber=request.getParameter('atlas');  // '6';

    var arrSearchFilters = new Array();
    arrSearchFilters[0] = new nlobjSearchFilter('tranid', 'custrecord_hein_insp_related_lease' , 'is', haAtlasNumber);


    var arrSearchColumns = new Array();
    arrSearchColumns[0] = new nlobjSearchColumn('custrecord_hein_insp_related_lease',null,null);
    arrSearchColumns[1] = new nlobjSearchColumn('custrecord_hein_insp_date',null,null);
    arrSearchColumns[2] = new nlobjSearchColumn('internalid',null,null);
    arrSearchColumns[3] = new nlobjSearchColumn('name',null,null);
    arrSearchColumns[4] = new nlobjSearchColumn('custrecord_hein_insp_inspector',null,null);
	arrSearchColumns[5] = new nlobjSearchColumn('custrecord_hein_insp_type',null,null);


    var arrSearchResults = nlapiSearchRecord('customrecord_hein_inspections', null, arrSearchFilters, arrSearchColumns);

     var htmlBody = '<body>';
 htmlBody += '<table class="tableHein" style="border-collapse: separate; border-spacing: 20px;">';

if (arrSearchResults != null && arrSearchResults.length > 0)
{
// Header
 htmlBody += '<tr>';
 htmlBody += ' <td> Name </td>';
 htmlBody += ' <td> Inspection Type </td>';
 htmlBody += ' <td> Inspector </td>';
 htmlBody += ' <td> Inspection Date </td>';
 htmlBody += ' <td> Related Lease </td>';
 htmlBody += '</tr>';
 htmlBody += '<p><br>';
 
    for ( var i in arrSearchResults) {
        var searchResult = arrSearchResults[i];

var haInspecName = searchResult.getValue('name',null,null);       
if(haInspecName == '' || haInspecName == null)
{
  var htmlBody = '<body>';
 htmlBody += '<table class="tableHein" style="border-collapse: separate; border-spacing: 20px;">';
 htmlBody += '<tr>';
 htmlBody += ' <td> No Results </td>';
 htmlBody += '</tr>';
break;
} 
else
{    

var haInspecInspector = searchResult.getText('custrecord_hein_insp_inspector',null,null);       
var haInspecLease = searchResult.getValue('custrecord_hein_insp_related_lease',null,null);
var haInspecType = searchResult.getText('custrecord_hein_insp_type',null,null);
var haInspecDate = searchResult.getValue('custrecord_hein_insp_date',null,null);
var haInternalID = searchResult.getText('internalid',null,null);
  haInspecLease = haInspecLease.split('-')[1];  
var linkURL = nlapiResolveURL('RECORD','customrecord_hein_inspections',haInternalID);

        htmlBody += '<tr>';
                htmlBody += ' <td><a href="'+ linkURL + '" target="_blank" >' + haInspecName  + '</td>';
   htmlBody += ' <td>' + haInspecType + '</td>';
   htmlBody += ' <td>' + haInspecInspector + '</td>';
   htmlBody += ' <td>' + haInspecDate + '</td>';
   htmlBody += ' <td>' + haInspecLease + '</td>';
   
   htmlBody += '</tr>';
    }
  }
}
else
{
 htmlBody += '<tr>';
 htmlBody += ' <td> No Results </td>';
 htmlBody += '</tr>';

}


 htmlBody += '</table>';
  htmlBody += '</body>';

    response.write(htmlBody);
 }
catch (e) {
            nlapiLogExecution("ERROR", "Inspection Search", "Error: " + e);
                         response.write(e);
        }

}

function gisMap(request, response){
    
    var haAtlasNumber= request.getParameter('atlas');  // '100777';

    var arrSearchFilters = new Array();
    arrSearchFilters[0] = new nlobjSearchFilter('mainline', null, 'is', 'T');
    arrSearchFilters[1] = new nlobjSearchFilter('tranid', null , 'is', haAtlasNumber);
    
    var arrSearchColumns = new Array();
    arrSearchColumns[0] = new nlobjSearchColumn('internalid',null,'group');
    
    var arrSearchResults = nlapiSearchRecord('transaction', null, arrSearchFilters, arrSearchColumns);
    
    for ( var i in arrSearchResults) {
        var searchResult = arrSearchResults[i];
        
    var haInternalID = searchResult.getText('internalid',null,'group');
    }
    var htmlBody = '<body>';
    htmlBody += '<iframe width="1300" height="900" src="https://gis.colorado.gov/atlas/FCFD3ADA-3517-45C3-A0DE-33EEA99B1ADC.htm?layer=lease&field=Internal_ID&value=';
        htmlBody += haInternalID;
 htmlBody += '"><p>Your browser does not support iframes.</p></iframe>';
    
    response.write(htmlBody);  
}


