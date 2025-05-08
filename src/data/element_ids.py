class ElementIDs:
    """Constants for all element IDs used in the application"""
    
    class Base:
        """Common elements used across multiple pages"""
        ALERT_ERROR = "alert-error"
        ALERT_SUCCESS = "alert-success"
    
    class Login:
        """Login page elements"""
        USER_ID = "login-user-id"
        PASSWORD = "login-password"
        SUBMIT = "login-submit"
        ACCOUNT_SIGNUP = "login-account-signup"
        ACCOUNT_TYPE = "tab-login-account-type-{}"
        LANGUAGE_DROPDOWN = "language-dropdown"
        LANGUAGE_OPTION = "language-option"
        RESET_PASSWORD = "reset-password-link"
    
    class Navigation:
        """Navigation elements"""
        ACCOUNT_SELECTOR = "account-selector"
        ACCOUNT_NAME = "account-name"
        ACCOUNT_ID = "account-id"
        ACCOUNT_DETAIL = "account-detail"
        SIDE_BAR_OPTION = "side-bar-option-{}"
    
    class Setting:
        """Setting panel elements"""
        SETTING_BUTTON = "setting-button"
        SETTING_OPTION = "setting-option-{}"
        SETTING_LANGUAGE = "setting-option-language"
    
    class Modals:
        """Modal elements"""
        # Demo Account Creation Modal
        DEMO_ACCOUNT_NAME = "demo-account-creation-modal-name"
        DEMO_ACCOUNT_EMAIL = "demo-account-creation-modal-email"
        DEMO_ACCOUNT_PHONE = "demo-account-creation-modal-phone"
        DEMO_ACCOUNT_CONFIRM = "demo-account-creation-modal-confirm"
        COUNTRY_DIAL_CODE = "country-dial-code"
        COUNTRY_DIAL_CODE_ITEM = "country-dial-code-item"
        COUNTRY_DIAL_CODE_SEARCH = "country-dial-code-search"
        DEPOSIT_DROPDOWN_ITEM = "deposit-dropdown-item"
        DEMO_ACCOUNT_DEPOSIT = "demo-account-creation-modal-deposit"
        DEMO_ACCOUNT_AGREEMENT = "demo-account-creation-modal-agreement-unchecked"
        
        # Demo Account Completion Modal
        DEMO_COMPLETION_TITLE = "demo-account-completion-modal-title"
        DEMO_COMPLETION_VALUE = "demo-completion-value"
        DEMO_COMPLETION_SIGN_IN = "demo-account-completion-modal-sign-in"
        
        # Feature Announcement Modal
        FEATURE_ANNOUNCEMENT_GOT_IT = "feature-announcement-modal-got-it-button"
        FEATURE_ANNOUNCEMENT_TRY_NOW = "feature-announcement-modal-try-it-now-button"
        
        # Change Password Modal
        CHANGE_PASSWORD_OLD = "change-password-modal-old-password"
        CHANGE_PASSWORD_NEW = "change-password-modal-new-password"
        CHANGE_PASSWORD_CONFIRM = "change-password-modal-confirm-new-password"
        CHANGE_PASSWORD_SUBMIT = "change-password-modal-confirm"
        
        # Input Field Validation
        INPUT_FIELD_VALIDATION = "input-field-validation"
    
    class Notifications:
        """Notification elements"""
        NOTIFICATION_SELECTOR = "notification-selector"
