class PrimaryKeys(object):
    primary_keys = {
        "Retention_Catalog_Terms": {
            "terms": {
                "_": [
                    [("termCode")]
                ]
            }
        },
        
        "Retention_Catalog_Sections": {
            "sections": {
                "_": [
                    [("sisSectionId")],
                    [("lmsSectionId")],
                    [("termCode"), ("sessionCode", "string", None), ("subjectCode"), ("sectionCourseNumber"), ("sectionNumber")],
                    [("termCode"), ("sectionRefNum")],
                ]
            }
        },
        
        "Retention_FacultyStaff_Staff": {
            "staff": {
                "_": [
                    [("facInd", "string", "N"), ("advInd", "string", "N"), ("staffInd", "string", "N")]
                ],
                "personItems": {
                    "_": [
                        [("personSisId")],
                        [("personLmsId")]
                    ],
                    "alternateIDs": {
                        "_": [
                            [("personAlternateIdType")]
                        ]
                    },
                    "PersonAddresses": {
                        "_": [
                            [("addressType"), ("addressStartDate", "date", None), ("addressEndDate", "date", None)]
                        ]
                    },
                    "PersonPhones": {
                        "_": [
                            [("phoneType")]
                        ]
                    },
                    "PersonEmails": {
                        "_": [
                            [("emailAddressType")]
                        ]
                    }
                }
            }
        },

        "Retention_FacultyStaff_AdvisingRelationship": {
            "advisors": {
                "_": [
                    [("advrId"), ("studentId"), ("advrTermCode"), ("advrType", "string", None)]
                ]
            }
        },
        
        "Retention_FacultyStaff_Teaching": {
            "teaching": {
                "_": [
                    [("personSisId"), ("sisSectionId")],
                    [("personLmsId"), ("sisSectionId")],
                    [("personSisId"), ("lmsSectionId")],
                    [("personLmsId"), ("lmsSectionId")],
                    [("personSisId"), ("termCode"), ("sessionCode", "string", None), ("subjectCode"), ("sectionCourseNumber"), ("sectionNumber")],
                    [("personLmsId"), ("termCode"), ("sessionCode", "string", None), ("subjectCode"), ("sectionCourseNumber"), ("sectionNumber")],
                    [("personSisId"), ("sectionRefNum")],
                    [("personLmsId"), ("sectionRefNum")]
                ]
            }
        },
        
        "Retention_StudentRecords_Students": {
            "students": {
                "_": [
                    [("studentCurrentStatus")]
                ],
                "personItems": {
                    "_": [
                        [("personSisId")],
                        [("personLmsId")]
                    ]
                },
                "studentTermItems": {
                    "_": [
                        [("personSisId")],
                        [("personLmsId")]
                    ]
                }
            }
        },
        
        "Retention_StudentRecords_StudentEnrollments": {
            "studentEnrollments": {
                "_": [
                    [("personSisId"), ("sisSectionId")],
                    [("personLmsId"), ("sisSectionId")],
                    [("personSisId"), ("lmsSectionId")],
                    [("personLmsId"), ("lmsSectionId")],
                    [("personSisId"), ("termCode"), ("sessionCode", "string", None), ("subjectCode"), ("sectionCourseNumber"), ("sectionNumber")],
                    [("personLmsId"), ("termCode"), ("sessionCode", "string", None), ("subjectCode"), ("sectionCourseNumber"), ("sectionNumber")],
                    [("personSisId"), ("sectionRefNum")],
                    [("personLmsId"), ("sectionRefNum")]
                ]
            }
        },

        "Retention_Engagement_Attendance": {
            "attendance": {
                "_": [
                    [("personSisId"), ("sisSectionId")],
                    [("personLmsId"), ("sisSectionId")],
                    [("personSisId"), ("lmsSectionId")],
                    [("personLmsId"), ("lmsSectionId")],
                    [("personSisId"), ("termCode"), ("sessionCode", "string", None), ("subjectCode"), ("sectionCourseNumber"), ("sectionNumber")],
                    [("personLmsId"), ("termCode"), ("sessionCode", "string", None), ("subjectCode"), ("sectionCourseNumber"), ("sectionNumber")],
                    [("personSisId"), ("sectionRefNum")],
                    [("personLmsId"), ("sectionRefNum")]
                ]
            }
        },
        
        "Retention_Engagement_Assignments": {
            "assignments": {
                "_": [
                    [("personSisId"), ("sisSectionId"), ("assignmentType"), ("assignmentLmsId")],
                    [("personLmsId"), ("sisSectionId"), ("assignmentType"), ("assignmentLmsId")],
                    [("personSisId"), ("lmsSectionId"), ("assignmentType"), ("assignmentLmsId")],
                    [("personLmsId"), ("lmsSectionId"), ("assignmentType"), ("assignmentLmsId")],
                    [("personSisId"), ("termCode"), ("sessionCode", "string", None), ("subjectCode"), ("sectionCourseNumber"), ("sectionNumber"), ("assignmentType"), ("assignmentLmsId")],
                    [("personLmsId"), ("termCode"), ("sessionCode", "string", None), ("subjectCode"), ("sectionCourseNumber"), ("sectionNumber"), ("assignmentType"), ("assignmentLmsId")],
                    [("personSisId"), ("sectionRefNum"), ("assignmentType"), ("assignmentLmsId")],
                    [("personLmsId"), ("sectionRefNum"), ("assignmentType"), ("assignmentLmsId")]
                ]
            }
        },
        
        "Retention_Engagement_EngagementActivity": {
            "engagementActivity": {
                "_": [
                    [("personSisId"), ("sisSectionId")],
                    [("personLmsId"), ("sisSectionId")],
                    [("personSisId"), ("lmsSectionId")],
                    [("personLmsId"), ("lmsSectionId")],
                    [("personSisId"), ("termCode"), ("sessionCode", "string", None), ("subjectCode"), ("sectionCourseNumber"), ("sectionNumber")],
                    [("personLmsId"), ("termCode"), ("sessionCode", "string", None), ("subjectCode"), ("sectionCourseNumber"), ("sectionNumber")],
                    [("personSisId"), ("sectionRefNum")],
                    [("personLmsId"), ("sectionRefNum")]
                ]
            }
        }
        
    }
