from oauthlib.oauth2 import OAuth2Token


class TokenManager:

    def __init__(self, logger=None, oauth2_token: OAuth2Token = None):
        self.logger = logger
        self.access_token = None
        self.expires_at = None
        if oauth2_token:
            self.load_from_oauth2_token(oauth2_token)

    def load_from_oauth2_token(self, oauth2_token: OAuth2Token = None):
        if self.logger:
            self.logger.debug(f"We got a token : {oauth2_token['access_token']}")
        self.access_token = oauth2_token['access_token']
        self.expires_at = oauth2_token['expires_at']
