class FranApiResources:
    login = 'login'
    # Franchisee
    addfraninv = 'dpt/fran/create-invoice'
    proackinv = 'dpt/fran/get-completed-invoices'
    acceptCInv = 'dpt/fran/accept-completed-invoice'
    procompletedinv = 'dpt/fran/get-completed-ackd-invoices'

    # Accounts
    getpvcinv = 'dpt/accounts/get-pvc-invoices'
    clearpvc = 'dpt/accounts/clear-pvc-invoice'
    updateimageclear = 'dpt/accounts/pvc-clear-image-complete'
    updatenameinflex = 'dpt/accounts/pvc-inv-name-complete'
    updatedistri = 'dpt/accounts/pvc-dist-complete'
    updateinvnumber = 'dpt/accounts/pvc-inv-num-complete'
    updateinvamt = 'dpt/accounts/pvc-inv-amt-complete'
    updateinvdate = 'dpt/accounts/pvc-inv-date-complete'
    processpvcinv = 'dpt/accounts/process-pvc-invoice'
    finalvalinv = 'dpt/accounts/get-final-validation-invoices'
    fvupdategrnamt = 'dpt/accounts/is-inv-grn-amt-complete'
    fvupdateisamt = 'dpt/accounts/is-grn-is-amt-complete'
    fvupdateistore = 'dpt/accounts/is-store-complete'
    fvupdatefree = 'dpt/accounts/is-free-articles-complete'
    clearFSInv = 'dpt/accounts/clear-is-validation'
    processFSInv = 'dpt/accounts/process-is'


    # Billing
    grnisinv = 'dpt/grn/get-grn-is-invoices'
    getgrnexs = 'dpt/grn/get-grn-executives'
    assigngrn = 'dpt/grn/assign-invoice-for-grn'
    assigntome = 'dpt/grn/get-assigned-to-me-invoices'
    uploadgrn = 'dpt/grn/upload-grn'
    assignis = 'dpt/grn/assign-invoice-for-is'
    uploadis = 'dpt/grn/upload-is'

