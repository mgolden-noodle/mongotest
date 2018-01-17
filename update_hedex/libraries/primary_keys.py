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
                            [("addressType", "string"),
                             ("addressStartDate", "date", None), ("addressEndDate", "date", None)]
                        ]
                    },
                    "PersonPhones": {
                        "_": [
                            [("phoneType", "string")]
                        ]
                    },
                    "PersonEmails": {
                        "_": [
                            [("emailAddressType", "string")]
                        ]
                    }
                }
            }
        } 
    }
