import os
from jwtdown_fastapi.authentication import Authenticator



class AccountAuthenticator(Authenticator):
    async def get_account_data():
        pass

    def get_account_getter():
        pass

    def get_hashed_password():
        pass


authenticator = AccountAuthenticator(os.environ["SIGNING_KEY"])