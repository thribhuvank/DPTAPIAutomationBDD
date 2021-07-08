import jsonpath
import requests
from behave import *

from payloads.franPayloads import *
from utilities.configurations import *
from utilities.resources import FranApiResources

use_step_matcher("re")


@given('store user login credentials are given')
def getUserCredentials(context):
    context.url = getConfig()['API']['baseurl'] + FranApiResources.login
    context.headers = {"Content-Type": "application/json"}
    context.data = getFranCredentials()


@when('try to login by using valid credentials')
def franLogin(context):
    context.response = requests.post(context.url, data=context.data, )


@then('user should login successfully')
def getAccessToken(context):
    context.json_response = context.response.json()
    fran_token = jsonpath.jsonpath(context.json_response, 'data.access_token')
    context.FRAN_ACCESSTOKEN = 'Bearer ' + fran_token[0]


@then('Verify response status should True')
def VerifyStatus(context):
    assert context.json_response['status']==True


@given('Invoice documents given in files')
def getInvoiceAttachments(context):
    context.url = getConfig()['API']['baseurl'] + FranApiResources.addfraninv
    context.file = getFiles()
    context.body = getFranIdasData()
    context.FRAN_ACCESSTOKEN = getFranAccessToken()
    context.header = {'Authorization': context.FRAN_ACCESSTOKEN}


@when('Upload invoice attachments')
def uploadInvoices(context):
    context.response = requests.post(context.url, headers=context.header, files=context.file, data=context.body, )
    print(context.response)


@then('verify response message')
def verifyResponseMessage(context):
    context.json_response = context.response.json()
    print(context.json_response['message'])


# Accounts
@given('Take accounts access token')
def getAccTokenPayLoads(context):
    context.url = getConfig()['API']['baseurl'] + FranApiResources.getpvcinv
    context.ACC_ACCESSTOKEN = getAccAccessToken()
    context.header = {'Authorization': context.ACC_ACCESSTOKEN}


@when('Get Invoices uploaded by franchisee')
def getPVCInvoicesAcc(context):
    context.response = requests.get(context.url, headers=context.header)
    print(context.response)


@then('Filter invoice id for specific franchisee')
def invoiceFilterByFranchisee(context):
    context.json_response = context.response.json()
    PVCInvoiceId = jsonpath.jsonpath(context.json_response, 'data.invoices[0].invoice_id')
    InvoiceId = PVCInvoiceId[0]
    print(InvoiceId)


# PVC
@given('Take accounts access token and payloads for pvc update')
def getPVCInvoiceIdForValidate(context):
    ACC_ACCESSTOKEN = getAccAccessToken()
    context.header = {'Authorization': ACC_ACCESSTOKEN}


@given('Take PVC invoice id')
def getPVCinvoiceIdAcc(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.getpvcinv
    response = requests.get(url, headers=context.header)
    json_response = response.json()
    PVCInvoiceId = jsonpath.jsonpath(json_response, 'data.invoices[0].invoice_id')
    context.InvoiceId = PVCInvoiceId[0]
    print(context.InvoiceId)
    context.body = getInvoiceId(context.InvoiceId)


@when('Clear specific PVC invoice updates')
def clearPVCInvUpdatesAcc(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.clearpvc
    context.response = requests.post(url, headers=context.header, data=context.body)
    print(context.response)


@when('Update Invoice image as clear')
def updateInvClearImageAcc(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.updateimageclear
    body = getUpdateClearImage(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@when('Update Invoice name in flex')
def updateInvNameFlexAcc(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.updatenameinflex
    body = getUpdateNameInFlex(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@when('Update Invoice distributor')
def updateInvDistriAcc(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.updatedistri
    body = getUpdateDistri(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@when('Update Invoice Number')
def updateInvNumberAcc(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.updateinvnumber
    body = getUpdateNumber(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@when('Update Invoice Amount')
def updateInvAmountAcc(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.updateinvamt
    body = getUpdateAmt(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@when('Update Invoice Date')
def updateInvDateAcc(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.updateinvdate
    body = getUpdateDate(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@when('Process pvc invoice')
def processPVCInvAcc(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.processpvcinv
    body = getInvoiceId(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@given('Take billing access token')
def getBillingTokenBill(context):
    context.url = getConfig()['API']['baseurl'] + FranApiResources.grnisinv
    context.param = getGRNISInv()
    context.BILL_ACCESSTOKEN = getBillAccessToken()
    context.header = {'Authorization': context.BILL_ACCESSTOKEN}


@when('Get GRN/IS Invoices uploaded by Accounts')
def getGRNISInvoicesBill(context):
    context.response = requests.get(context.url, headers=context.header, params=context.param)
    print(context.response)


# GRN
@given('Take billing access token and payloads')
def getBillTokenPayloadsBill(context):
    context.url = getConfig()['API']['baseurl'] + FranApiResources.getgrnexs
    context.BILL_ACCESSTOKEN = getBillAccessToken()
    context.header = {'Authorization': context.BILL_ACCESSTOKEN}


@when('Get executives for GRN')
def getExforGRNBill(context):
    context.response = requests.get(context.url, headers=context.header)
    print(context.response)


@then('Filter executive id for grn assignment')
def getExIDforGRNBill(context):
    context.json_response = context.response.json()
    GRNUserId = jsonpath.jsonpath(context.json_response, 'data[0].user_id')
    context.UserId = GRNUserId[0]
    print(context.UserId)


# GRN Assign
@given('Take billing access token and payloads for grnis assign')
def getGRNISInvoiceIdBill(context):
    context.grn_url = getConfig()['API']['baseurl'] + FranApiResources.assigngrn
    context.is_url = getConfig()['API']['baseurl'] + FranApiResources.assignis
    BILL_ACCESSTOKEN = getBillAccessToken()
    context.header = {'Authorization': BILL_ACCESSTOKEN}


@given('Take invoice id for grn assign')
def getInvoiceIdforGrnAssignBill(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.grnisinv
    param = getGRNISInv()
    inv_response = requests.get(url, headers=context.header, params=param)
    BInvoiceId = jsonpath.jsonpath(inv_response.json(), 'data.invoices[0].invoice_id')
    context.InvoiceId = BInvoiceId[0]
    print(context.InvoiceId)


@given('Get executive id for assign')
def getUserIdforGRNAssignBill(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.getgrnexs
    userid_response = requests.get(url, headers=context.header)
    json_userid_response = userid_response.json()
    GRNUserId = jsonpath.jsonpath(json_userid_response, 'data[0].user_id')
    context.UserId = GRNUserId[0]
    print(context.UserId)
    context.body = getAssignGRN(context.InvoiceId, context.UserId)


@when('Assign Executive for GRN Invoice')
def assignExGRNBill(context):
    context.response = requests.post(context.grn_url, headers=context.header, data=context.body)
    print(context.response)


# Upload GRN Document
@given('Take billing executive access token and payloads for grn/is upload')
def getGRNAsnToMeBillEx(context):
    context.grn_url = getConfig()['API']['baseurl'] + FranApiResources.uploadgrn
    context.is_url = getConfig()['API']['baseurl'] + FranApiResources.uploadis
    BIEX_ACCESSTOKEN = getBillExAccessToken()
    context.header = {'Authorization': BIEX_ACCESSTOKEN}
    context.grn_file = getGRNFiles()
    context.is_file = getISFiles()


@given('Take invoice id for grn/is document upload')
def getInvoiceIdforGRNISUploadBEx(context):
    asn_url = getConfig()['API']['baseurl'] + FranApiResources.assigntome
    param = getGRNAToMe()
    BIEX_ACCESSTOKEN = getBillExAccessToken()
    context.header = {'Authorization': BIEX_ACCESSTOKEN}
    awtGRNASN = requests.get(asn_url, headers=context.header, params=param)
    GRNEXInvoiceId = jsonpath.jsonpath(awtGRNASN.json(), 'data.invoices[0].invoice_id')
    context.InvoiceId = GRNEXInvoiceId[0]
    print(context.InvoiceId)



@when('Upload GRN document')
def uploadGRNBEx(context):
    context.response = requests.post(context.grn_url, headers=context.header, data=context.body, files=context.grn_file)
    print(context.response)


@when('Assign Executive for IS Invoice')
def assignExGRNBEx(context):
    BIEX_ACCESSTOKEN = getBillExAccessToken()
    header = {'Authorization': BIEX_ACCESSTOKEN}
    context.response = requests.post(context.is_url, headers=header, data=context.body)
    print(context.response)


@when('Upload IS document')
def uploadISBEx(context):
    context.response = requests.post(context.is_url, headers=context.header, data=context.body, files=context.is_file)
    print(context.response)


# Final Validation
@given('Take accounts access token and get final validation payloads')
def getFVInvoicesAccFS(context):
    context.url = getConfig()['API']['baseurl'] + FranApiResources.finalvalinv
    context.param = getFVInv()
    ACC_ACCESSTOKEN = getAccAccessToken()
    context.header = {'Authorization': ACC_ACCESSTOKEN}


@when('Find Final validation invoice id')
def getFVInvoiceIdAFS(context):
    context.response = requests.get(context.url, headers=context.header, params=context.param)
    print(context.response)
    FVISInvoice = jsonpath.jsonpath(context.response.json(), 'data.invoices[0].invoice_id')
    context.InvoiceId = FVISInvoice[0]
    print(context.InvoiceId)


# update FV
@given('Get accounts access token and payloads for update final validation')
def getFVInvoiceAccFSVal(context):
    context.url = getConfig()['API']['baseurl'] + FranApiResources.finalvalinv
    context.param = getFVInv()
    ACC_ACCESSTOKEN = getAccAccessToken()
    context.header = {'Authorization': ACC_ACCESSTOKEN}


@given('Get invoice id for final validation after grn/is')
def getFVInvoiceAFRGRNIS(context):
    response = requests.get(context.url, headers=context.header, params=context.param)
    FVISInvoice = jsonpath.jsonpath(response.json(), 'data.invoices[0].invoice_id')
    context.InvoiceId = FVISInvoice[0]
    print(context.InvoiceId)


@when('Update GRN amt is equal to Invoice amt')
def updateFsGRNAmtACCFS(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.fvupdategrnamt
    body = getFSGrnAmt(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@when('Update Is amt is equal to GRN amt')
def updateFsISAmtACCFS(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.fvupdateisamt
    body = getFSISAmt(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@when('Update Invoice in Store name')
def updateFsIsStoreACCFS(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.fvupdateistore
    body = getFSIsStore(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@when('Update Free articles in invoice')
def updateFsFreeACCFS(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.fvupdatefree
    body = getFSIsFree(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@when('Clear Final validation')
def clearFSinvACCFS(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.clearFSInv
    body = getInvoiceId(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


@when('Process final validation invoice')
def processFSinvACCFS(context):
    url = getConfig()['API']['baseurl'] + FranApiResources.processFSInv
    body = getInvoiceId(context.InvoiceId)
    context.response = requests.post(url, headers=context.header, data=body)
    print(context.response)


# ack invoice
@given('Get franchisee access token and payloads for approve Ack Invoice')
def getPCAckInvoicesFRAN(context):
    context.url = getConfig()['API']['baseurl'] + FranApiResources.acceptCInv
    FRAN_ACCESSTOKEN = getFranAccessToken()
    context.header = {'Authorization': FRAN_ACCESSTOKEN}


@given('Get invoice id for approve ack from franchisee')
def getPCAckInvoiceIdFRAN(context):
    pcAck_url = getConfig()['API']['baseurl'] + FranApiResources.proackinv
    param = getCACKInv()
    fv_response = requests.get(pcAck_url, headers=context.header, params=param)
    FCIvcId = jsonpath.jsonpath(fv_response.json(), 'data.invoices[0].invoice_id')
    context.InvoiceId = FCIvcId[0]
    print(context.InvoiceId)
    context.body = getInvoiceId(context.InvoiceId)


@when('Accept Process Completed invoice')
def acceptFCInvFRAN(context):
    context.response = requests.post(context.url, headers=context.header, data=context.body)
    print(context.response)


# completed invoice
@given('Get franchisee access token and payloads')
def getPCInvoicesFRANC(context):
    context.url = getConfig()['API']['baseurl'] + FranApiResources.procompletedinv
    context.param = getCACKInv()
    FRAN_ACCESSTOKEN = getFranAccessToken()
    context.header = {'Authorization': FRAN_ACCESSTOKEN}


@when('View process completed and ack invoices')
def getPCInvoiceIdFRCOM(context):
    context.response = requests.get(context.url, headers=context.header, params=context.param)
    print(context.response)
    FCId = jsonpath.jsonpath(context.response.json(), 'data.invoices[0].invoice_id')
    context.InvoiceId = FCId[0]
    print(context.InvoiceId)




