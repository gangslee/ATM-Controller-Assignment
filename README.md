# ATM-Controller-Assignment

## Classes

### Bank

**Properties**
- **data** - Data consists of card ID, pin, accounts, balance of each accounts

**Methods**

- **add_data** : Add new data with new card_id, pin, accounts
- **add_account** : Add new account of exist card_id & pin
- **auth_info** : Authorize input info with card_id & pin
- **update_data** : Update account's balance data

### AtmController

**Properties**
- **bank** - Data of ATM's Bank
- **card_id** - Card ID which authorized by Bank
- **pin** - PIN which authorized by Bank
- **accounts** - Data of Accounts and balance of each accounts 

**Methods**

- **get_accounts** : Get accounts from Bank
- **select_account** : Select accounts which will used
- **see_balance** : See balance of selected account
- **deposit** : Deposit cash from selected account
- **withdraw** : Withdraw cash from selected account


## Tests

### bankTest
**Unittest logic of Bank's methods with unittest module**

### atmControllerTest
**Unittest logic of AtmController's methods with unittest module**


