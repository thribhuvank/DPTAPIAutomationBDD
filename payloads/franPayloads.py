def getFranCredentials():
    data = {'username': '9880308886', 'password': 'shop@2021'}
    return data


def getFiles():
    test_file_1 = open("G:/API/1.jpg", "rb").read()
    file = {"invoice_attachments[]": test_file_1}
    return file


def getFranIdasData():
    values = {'fran_id': '1'}
    return values


def getInvoiceId(InvoiceId):
    body = {'invoice_id': InvoiceId}
    return body


def getUpdateClearImage(InvoiceId):
    body = {'invoice_id': InvoiceId, 'invoice_image_clear': '1'}
    return body


def getUpdateNameInFlex(InvoiceId):
    body = {'invoice_id': InvoiceId, 'invoice_name_flex': '1'}
    return body


def getUpdateDistri(InvoiceId):
    body = {'invoice_id': InvoiceId, 'dist_gst': '29AAXFS8411J1ZD', 'dist_id': '5d889c48b2ffe848e74d8128'}
    return body


def getUpdateNumber(InvoiceId):
    body = {'invoice_id': InvoiceId, 'invoice_number': 'SB10001'}
    return body


def getUpdateAmt(InvoiceId):
    body = {'invoice_id': InvoiceId, 'invoice_amount': '1200'}
    return body


def getUpdateDate(InvoiceId):
    body = {'invoice_id': InvoiceId, 'invoice_date': '2021-05-15'}
    return body


def getGRNISInv():
    param = {"page": "1", "recordperpage": "12", "franchisee": "1", "month_of": "05"}
    return param


def getAssignGRN(InvoiceId, UserId):
    body = {'invoice_id': InvoiceId, 'user_id': UserId}
    return body


def getGRNAToMe():
    param = {"page": "1", "recordsPerPage": "12", "month_of": "05"}
    return param


def getGRNFiles():
    grn_file_1 = open("G:/API/1.jpg", "rb").read()
    file = {'grn_attachments[]': grn_file_1}
    return file


def getISFiles():
    is_file_1 = open("G:/API/1.jpg", "rb").read()
    file = {'is_attachments[]': is_file_1}
    return file


def getFVInv():
    param = {"page": "1", "recordperpage": "12", "month_of": "05"}
    return param


def getFSGrnAmt(InvoiceId):
    body = {'invoice_id': InvoiceId, 'invoice_grn_amt': '1'}
    return body


def getFSISAmt(InvoiceId):
    body = {'invoice_id': InvoiceId, 'grn_is_amt': '1'}
    return body


def getFSIsStore(InvoiceId):
    body = {'invoice_id': InvoiceId, 'is_store': '1'}
    return body


def getFSIsFree(InvoiceId):
    body = {'invoice_id': InvoiceId, 'free_articles': '1'}
    return body


def getCACKInv():
    param = {"page": "1", "recordperpage": "12", "month_of": "05", "fran_id":"1"}
    return param


