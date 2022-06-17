"""Withdrawal Dialog."""

import sys
import questionary


def make_withdrawal(account):
    """Withdrawal Dialog."""

    # @TODO:  Use questionary to capture the withdrawal and set it equal to amount variable. Be sure that amount is a floating point number.
    withdraw_amount = float(questionary.text("Insert withdrawal amount here:").ask())

    # @TODO:  Validates amount of withdrawal. If less than or equal to 0 system exits with error message.
    if withdraw_amount <= 0:
        print("Error: amount not recognized")

    # @TODO: Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
    # Else system exits with error messages indicating that the account is short of funds.
    elif withdraw_amount <= account["balance"]:
        account["balance"] = account["balance"] - withdraw_amount
        return account
    else: 
        print("Error: account is short of funds.")