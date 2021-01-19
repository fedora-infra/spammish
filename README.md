# Spammish Accounts

This is a UI to manage accounts detected as spam in Fedora's authentication system.

When a users registers for a new account in Noggin and Basset is enabled, the account is created as "stage user" but the email validation token is not sent out. Instead, a message is sent to Basset to request a spam check. Basset sends a request back to Noggin with the result. If the account is not flagged as spam, the validation email is sent out. Otherwise, the account stays in the "stage" state.

This application lets admins review accounts marked as spam, and accept or deny their request. It sends the message to Noggin which will proceed with the email validation system if the account is not spam.
