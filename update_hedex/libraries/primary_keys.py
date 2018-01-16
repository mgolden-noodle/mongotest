class PrimaryKeys(object):
    primary_keys = {
        "Retention_FacultyStaff_Staff": {
            "staff": {
                "_": [
                    [("facInd", "string", "N"), ("advInd", "string", "N"), ("staffInd", "string", "N")]
                ],
                "personItems": {
                    "_": [
                        [("personSisId", "string")],
                        [("personLmsId", "string")]
                    ],
                    "alternateIDs": {
                        "_": [
                            [("personAlternateIdType", "string")]
                        ]
                    },
                    "PersonAddresses": {
                        "_": [
                            [("addressType", "string"), ("addressLine1", "string"),
                             ("city", "string"), ("state", "string"), ("postalCode", "string"), ("country", "string", None),
                             ("addressStartDate", "date", None), ("addressEndDate", "date", None)]
                        ]
                    },
                    "PersonPhones": {
                        "_": [
                            [("phoneNumber", "string"), ("phoneType", "string"), ("phoneExtension", "string")]
                        ]
                    },
                    "PersonEmails": {
                        "_": [
                            [("emailAddress", "string"), ("emailAddressType", "string")]
                        ]
                    }
                }
            }
        } 
    }
