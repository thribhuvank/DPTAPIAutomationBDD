# Created by Owner at 14/05/2021
Feature: DPT Functional Testing
  # Enter feature description here
  @Fran
  Scenario: Franchisee login with valid credentials
    Given store user login credentials are given
    When try to login by using valid credentials
    Then user should login successfully
    And Verify response status should True

  @Fran
  Scenario: Add invoice attachment from franchisee
    Given Invoice documents given in files
    When Upload invoice attachments
    Then verify response message
    And Verify response status should True

  @PVC
  Scenario: Accounts Get PVC invoices
    Given Take accounts access token
    When Get Invoices uploaded by franchisee
    Then Filter invoice id for specific franchisee
    And Verify response status should True

  @PVC
  Scenario: Accounts clear PVC updates
    Given Take accounts access token and payloads for pvc update
    And Take PVC invoice id
    When Clear specific PVC invoice updates
    Then verify response message
    And Verify response status should True

  @PVC
  Scenario: Accounts update pvc clear image
    Given Take accounts access token and payloads for pvc update
    And Take PVC invoice id
    When Update Invoice image as clear
    Then verify response message
    And Verify response status should True

  @PVC
  Scenario: Accounts update pvc invoice in flex name
    Given Take accounts access token and payloads for pvc update
    And Take PVC invoice id
    When Update Invoice name in flex
    Then verify response message
    And Verify response status should True

  @PVC
  Scenario: Accounts update pvc invoice distributor
    Given Take accounts access token and payloads for pvc update
    And Take PVC invoice id
    When Update Invoice distributor
    Then verify response message
    And Verify response status should True

  @PVC
  Scenario: Accounts update pvc invoice number
    Given Take accounts access token and payloads for pvc update
    And Take PVC invoice id
    When Update Invoice Number
    Then verify response message
    And Verify response status should True

  @PVC
  Scenario: Accounts update pvc invoice amount
    Given Take accounts access token and payloads for pvc update
    And Take PVC invoice id
    When Update Invoice Amount
    Then verify response message
    And Verify response status should True

  @PVC
  Scenario: Accounts update pvc invoice date
    Given Take accounts access token and payloads for pvc update
    And Take PVC invoice id
    When Update Invoice Date
    Then verify response message
    And Verify response status should True

  @PVC
  Scenario: Accounts update process pvc invoice
    Given Take accounts access token and payloads for pvc update
    And Take PVC invoice id
    When Process pvc invoice
    Then verify response message
    And Verify response status should True

  @BillingAdmin
  Scenario: Billing get GRN/IS invoices
    Given Take billing access token
    When Get GRN/IS Invoices uploaded by Accounts
    Then Filter invoice id for specific franchisee
    And Verify response status should True

  @BillingAdmin
  Scenario: Billing get executive for grn
    Given Take billing access token and payloads
    When Get executives for GRN
    Then Filter executive id for grn assignment
    And Verify response status should True

  @BillingAdmin
  Scenario: Billing assign executive for grn
    Given Take billing access token and payloads for grnis assign
    And Take invoice id for grn assign
    And Get executive id for assign
    When Assign Executive for GRN Invoice
    Then verify response message
    And Verify response status should True

  @BillingEx
  Scenario: Billing Executive upload GRN document
    Given Take billing executive access token and payloads for grn/is upload
    And Take invoice id for grn/is document upload
    And Get executive id for assign
    When Upload GRN document
    Then verify response message
    And Verify response status should True

  @BillingEx
  Scenario: Billing assign executive for IS
    Given Take billing access token and payloads for grnis assign
    And Take invoice id for grn assign
    And Get executive id for assign
    When Assign Executive for IS Invoice
    Then verify response message
    And Verify response status should True

  @BillingEx
  Scenario: Billing Executive upload IS document
    Given Take billing executive access token and payloads for grn/is upload
    And Take invoice id for grn/is document upload
    And Get executive id for assign
    When Upload IS document
    Then verify response message
    And Verify response status should True

  @AfterIS
  Scenario: Accounts Get Invoice for final validation after GRN/IS
    Given Take accounts access token and get final validation payloads
    When Find Final validation invoice id
    Then verify response message
    And Verify response status should True

  @AfterIS
  Scenario: Accounts update final validation after GRN/IS
    Given Get accounts access token and payloads for update final validation
    And Get invoice id for final validation after grn/is
    When Clear Final validation
    Then verify response message
    And Verify response status should True

  @AfterIS
  Scenario: Accounts update final validation after GRN/IS
    Given Get accounts access token and payloads for update final validation
    And Get invoice id for final validation after grn/is
    When Update GRN amt is equal to Invoice amt
    Then verify response message
    And Verify response status should True

  @AfterIS
  Scenario: Accounts update final validation after GRN/IS
    Given Get accounts access token and payloads for update final validation
    And Get invoice id for final validation after grn/is
    When Update Is amt is equal to GRN amt
    Then verify response message
    And Verify response status should True

  @AfterIS
  Scenario: Accounts update final validation after GRN/IS
    Given Get accounts access token and payloads for update final validation
    And Get invoice id for final validation after grn/is
    When Update Invoice in Store name
    Then verify response message
    And Verify response status should True

  @AfterIS
  Scenario: Accounts update final validation after GRN/IS
    Given Get accounts access token and payloads for update final validation
    And Get invoice id for final validation after grn/is
    When Update Free articles in invoice
    Then verify response message
    And Verify response status should True

  @AfterIS
  Scenario: Accounts update final validation after GRN/IS
    Given Get accounts access token and payloads for update final validation
    And Get invoice id for final validation after grn/is
    When Process final validation invoice
    Then verify response message
    And Verify response status should True

  @Franchisee
  Scenario: Franchisee Get Awaiting Acknowledgement and Completed Invoices
    Given Get franchisee access token and payloads for approve Ack Invoice
    And Get invoice id for approve ack from franchisee
    When Accept Process Completed invoice
    Then verify response message
    And Verify response status should True

  @Franchisee
  Scenario: Franchisee Get Awaiting Acknowledgement and Completed Invoices
    Given Get franchisee access token and payloads
    When View process completed and ack invoices
    Then verify response message
    And Verify response status should True





