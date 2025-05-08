class UIMessages:
    """Constants for all UI text messages including error messages, notifications, and popup text"""
    
    # ===== Alert Error Messages =====
    LOGIN_INVALID_CREDENTIALS = "Invalid credentials, please try again"

    # ==== Demo Creation Error Messages ====
    IS_REQUIRED = "{} is required"
    ACCEPT_TERM_CONDITION = "Please review and accept the Terms and Conditions"
    EMAIL_FORMAT_INVALID = "Email format invalid"
    PHONE_NUMBER_INVALID = "Phone number is invalid"

    # -- Password Change Error Messages --
    PASSWORD_INVALID_FORMAT = (
        "Password format is incorrect. Password must include at least 12-20 characters, "
        "including 1 capital letter, 1 small letter, 1 number, 1 special characters."
    )
    PASSWORD_CONFIRMATION_MISMATCH = "New password does not match confirm password"
    PASSWORD_CURRENT_INVALID = "Invalid current password"
    PASSWORD_SAME_AS_OLD = "New password and old password are the same"
    PASSWORD_PREVIOUSLY_USED = "New password cannot be the same as previous 5 old password"
    
    # ===== Alert Success Messages =====
    PASSWORD_UPDATE_SUCCESS = "Account password has been updated successfully."
    
    # ===== Notification Messages =====
    DEMO_ACCOUNT_READY = "Your Demo Account is Ready!"
    # trade confirmation
    MARKET_ORDER_SUBMITTED = "Market Order Submitted"

