# NHANES Dataset Codebook & Reference Guide

## Dataset Overview

**Source:** National Health and Nutrition Examination Survey (NHANES)  
**Survey Cycle:** 2021-2023  
**Conducted by:** CDC's National Center for Health Statistics  
**Purpose:** Assess health and nutritional status of adults and children in the United States  
**Sample Size:** ~11,000+ participants

---

## Standard NHANES Coding Scheme

### Universal Response Codes
```
1 = Yes
2 = No
7 = Refused (participant refused to answer)
9 = Don't know
Empty/blank = Question not applicable or skipped
```

### Frequency Response Codes (for "How often" questions)
```
0 = Never
1 = Several days / Rarely
2 = More than half the days / Sometimes
3 = Nearly every day / Most times
4 = Always
```

### Difficulty Level Codes (Functioning questions)
```
1 = No difficulty
2 = Some difficulty
3 = A lot of difficulty
4 = Cannot do at all
```

---

## Dataset-Specific Code Definitions

### 1. ACCULTURATION (`acculturation.csv`)
**Purpose:** Language use and cultural adaptation

| Variable | Values | Meaning |
|----------|--------|---------|
| `LanguageSpokenAtHome_1/2/3` | 1 | English |
| | 2 | Spanish |
| | 3+ | Other languages |
| | 9 | Refused |
| `RatioEnglishSpanishAtHome` | 1 | Only Spanish |
| | 2 | More Spanish than English |
| | 3 | Both equally |
| | 4 | More English than Spanish |
| | 5 | Only English |

---

### 2. ALCOHOL USE (`alcohol_use.csv`)
**Purpose:** Alcohol consumption patterns and history

| Variable | Values | Meaning |
|----------|--------|---------|
| `EverHad_Alcohol` | 1 | Yes |
| | 2 | No |
| `AlcoholConsumptionFrequency_12Months` | 1 | Every day |
| | 2 | Nearly every day |
| | 3 | 3-4 times/week |
| | 4 | 2 times/week |
| | 5 | Once/week |
| | 6 | 2-3 times/month |
| | 7 | Once/month |
| | 8 | 7-11 times/year |
| | 9 | 3-6 times/year |
| | 10 | 1-2 times/year |
| `DailyHeavyDrinkingHistory` | 1 | Yes, had period of daily heavy drinking |
| | 2 | No |
| `AverageDrinksPerDrinkingDay_12Months` | continuous | Actual number of drinks |
| `OccasionsWithHeavyDrinking_30Days` | continuous | Number of occasions |

---

### 3. AUDIOMETRY (`audiometry.csv`)
**Purpose:** Hearing status and hearing loss

| Variable | Values | Meaning |
|----------|--------|---------|
| `HearingStatus_NoAid` | 1 | Excellent |
| | 2 | Good |
| | 3 | Little trouble |
| | 4 | Moderate trouble |
| | 5 | A lot of trouble |
| | 6 | Deaf |
| `DifficultyHearing_WithBackgroundNoise` | 1 | Always |
| | 2 | Usually |
| | 3 | About half the time |
| | 4 | Seldom |
| | 5 | Never |
| `LastHearingTest_Specialist` | 1 | Less than 1 year ago |
| | 2 | 1-4 years ago |
| | 3 | 5-9 years ago |
| | 4 | 10+ years ago |
| | 5 | Never |

---

### 4. BLOOD PRESSURE & CHOLESTEROL (`blood_pressure_cholesterol.csv`)
**Purpose:** Cardiovascular health indicators

| Variable | Values | Meaning |
|----------|--------|---------|
| `EverTold_Hypertension` | 1 | Yes |
| | 2 | No |
| `ConfirmedHypertension_Visits` | 1 | Yes (told on 2+ visits) |
| | 2 | No |
| `CurrentlyTaking_BloodPressureMedication` | 1 | Yes |
| | 2 | No |
| `EverTold_HighCholesterol` | 1 | Yes |
| | 2 | No |
| `CurrentlyTaking_CholesterolMedication` | 1 | Yes |
| | 2 | No |

---

### 5. CURRENT HEALTH STATUS (`current_health_status.csv`)
**Purpose:** General health and HIV testing

| Variable | Values | Meaning |
|----------|--------|---------|
| `EverTestedFor_AIDS` | 1 | Yes |
| | 2 | No |

---

### 6. DERMATOLOGY (`dermatology.csv`)
**Purpose:** Sun exposure and skin protection behaviors

| Variable | Values | Meaning |
|----------|--------|---------|
| `ShadeStayingFrequency` | 1 | Always |
| | 2 | Most of the time |
| | 3 | Sometimes |
| | 4 | Rarely |
| | 5 | Never |
| `WearsLongSleevesFrequency` | 1-5 | Same as above |
| `UsesSunscreenFrequency` | 1-5 | Same as above |

---

### 7. DIABETES (`diabetes.csv`)
**Purpose:** Diabetes diagnosis and treatment

| Variable | Values | Meaning |
|----------|--------|---------|
| `EverTold_Diabetes` | 1 | Yes |
| | 2 | No |
| | 3 | Borderline/Prediabetes |
| `Age_DiabetesDiagnosis` | continuous | Age in years |
| `CurrentlyTaking_Insulin` | 1 | Yes |
| | 2 | No |
| `InsulinDuration` | continuous | Duration in time units |
| `CurrentlyTaking_DiabeticPills` | 1 | Yes |
| | 2 | No |
| `EverTold_Prediabetes` | 1 | Yes |
| | 2 | No |
| `BloodSugarTest_Last3Years` | 1 | Yes |
| | 2 | No |
| | 9 | Don't know |


---

### 8. DIET BEHAVIOR & NUTRITION (`diet_behavior_nutrition.csv`)
**Purpose:** Dietary habits, breastfeeding, school meals

| Variable | Values | Meaning |
|----------|--------|---------|
| `EverBreastfed` | 1 | Yes |
| | 2 | No |
| `AgeStoppedBreastfeeding` | continuous | Age in months |
| `AgeFirstFedFormula` | continuous | Age in months |
| `CurrentlyAttendingSchool` | 1 | Yes |
| | 2 | No |
| `SchoolServesLunches` | 1 | Yes |
| | 2 | No |
| `LunchCostStatus` | 1 | Free |
| | 2 | Reduced price |
| | 3 | Full price |
| `BreakfastCostStatus` | 1 | Free |
| | 2 | Reduced price |
| | 3 | Full price |
| `MealPlanningResponsibility` | 1 | Yes |
| | 2 | No |

---

### 9. EARLY CHILDHOOD (`early_childhood.csv`)
**Purpose:** Birth weight and childhood health

| Variable | Values | Meaning |
|----------|--------|---------|
| `BirthWeight_1` | continuous | Weight in pounds |
| `BirthWeight_2` | continuous | Weight in ounces |
| `Weight_1` | 1 | Less than 5.5 lbs |
| | 2 | 5.5 - 9.0 lbs |
| | 3 | More than 9.0 lbs |
| `OverweightDiagnosis` | 1 | Yes |
| | 2 | No |

---

### 10. FUNCTIONING (`functioning.csv`)
**Purpose:** Disability assessment and functional limitations

| Variable | Values | Meaning |
|----------|--------|---------|
| `DifficultySeeingWithGlasses_Level` | 1 | No difficulty |
| | 2 | Some difficulty |
| | 3 | A lot of difficulty |
| | 4 | Cannot do at all |
| `DifficultyHearingWithAid_Level` | 1-4 | Same as above |
| `DifficultyWalkingClimbingSteps_Level` | 1-4 | Same as above |
| `DifficultyCommunicating_Level` | 1-4 | Same as above |
| `DifficultyRememberingConcentrating_Level` | 1-4 | Same as above |
| `DifficultySelfCare_Level` | 1-4 | Same as above |
| `FrequencyWorriedAnxious` | 1 | Daily |
| | 2 | Weekly |
| | 3 | Monthly |
| | 4 | A few times a year |
| | 5 | Never |
| `LevelOfWorryAnxiety` | 1 | Not at all |
| | 2 | A little |
| | 3 | Somewhat |
| | 4 | Very much |
| | 5 | So much I couldn't work |

---

### 11. HEALTH INSURANCE (`health_insurance.csv`)
**Purpose:** Health insurance coverage

| Variable | Values | Meaning |
|----------|--------|---------|
| `Has_HealthInsurance` | 1 | Yes |
| | 2 | No |
| `HealthInsurance_Private` | 1 | Yes |
| | 2 | No |
| `HealthInsurance_Medicare` | 1 | Yes |
| | 2 | No |
| `HealthInsurance_Medicaid` | 1 | Yes |
| | 2 | No |
| `HealthInsurance_CHIP` | 1 | Yes (Children's Health Insurance Program) |
| | 2 | No |
| `HealthInsurance_Military` | 1 | Yes (Tricare/VA) |
| | 2 | No |
| `NoHealthInsurance_Past12Months` | 1 | Yes |
| | 2 | No |

---

### 12. HEPATITIS (`hepatitis.csv`)
**Purpose:** Hepatitis B status

| Variable | Values | Meaning |
|----------|--------|---------|
| `EverTold_HepatitisB` | 1 | Yes |
| | 2 | No |

---

### 13. HOSPITAL UTILIZATION & ACCESS TO CARE (`hospital_utilization_access_to_care.csv`)
**Purpose:** Healthcare access and usage

| Variable | Values | Meaning |
|----------|--------|---------|
| `GeneralHealth_Status` | 1 | Excellent |
| | 2 | Very good |
| | 3 | Good |
| | 4 | Fair |
| | 5 | Poor |
| `HasUsualPlace_ForCare` | 1 | Yes |
| | 2 | No (more than one place) |
| | 3 | No (no place) |
| `UsualPlace_Type` | 1 | Doctor's office/health center |
| | 2 | Urgent care/clinic |
| | 3 | Emergency room |
| | 4 | VA Medical Center |
| | 5 | Other |
| `TelehealthAppointment_Past12Months` | 1 | Yes |
| | 2 | No |
| `MentalHealthVisit_Past12Months` | 1 | Yes |
| | 2 | No |


---

### 14. HOUSING CHARACTERISTICS (`housing_characteristics.csv`)
**Purpose:** Home environment

| Variable | Values | Meaning |
|----------|--------|---------|
| `NumberOfRooms_Home` | continuous | Count of rooms |

---

### 15. IMMUNIZATION (`immunization.csv`)
**Purpose:** Vaccination history

| Variable | Values | Meaning |
|----------|--------|---------|
| `EverReceived_HepatitisAVaccine` | 1 | Yes |
| | 2 | No |
| | 9 | Don't know |
| `EverReceived_HPVTreatment_Girls` | 1 | Yes |
| | 2 | No |
| | 9 | Don't know |
| `EverReceived_HPVTreatment_Boys` | 1 | Yes |
| | 2 | No |
| | 9 | Don't know |
| `AgeAtFirstHPVDose` | continuous | Age in years |
| `NumberOfHPVDosesReceived` | continuous | Count (1-3) |

---

### 16. INCOME (`income.csv`)
**Purpose:** Financial status and poverty level

| Variable | Values | Meaning |
|----------|--------|---------|
| `MoreThan5000_InSavings` | 1 | Yes |
| | 2 | No |
| `TotalSavings_CashAssets` | 1 | $0 - $4,999 |
| | 2 | $5,000 - $19,999 |
| | 3 | $20,000+ |
| `FamilyPovertyLevelIndex_Ratio` | continuous | Ratio (0-5+) |
| | <1.0 | Below poverty line |
| | 1.0-1.99 | Low income |
| | 2.0+ | Above low income |

---

### 17. KIDNEY CONDITION - UROLOGY (`kidney_condition_urology.csv`)
**Purpose:** Kidney health and urinary issues

| Variable | Values | Meaning |
|----------|--------|---------|
| `UrineLeakageFrequency` | 1 | Never |
| | 2 | Less than once a month |
| | 3 | A few times a month |
| | 4 | A few times a week |
| | 5 | Every day/night |
| `UrineLeakageAmount` | 1 | Drops |
| | 2 | Small splashes |
| | 3 | More |
| `EverTold_KidneyFailure` | 1 | Yes |
| | 2 | No |
| `DialysisReceived_12Months` | 1 | Yes |
| | 2 | No |
| `NightUrinationFrequency_30Days` | continuous | Number of times per night |

---

### 18. MEDICAL CONDITIONS (`medical_conditions.csv`)
**Purpose:** Chronic diseases and medical history

| Variable | Values | Meaning |
|----------|--------|---------|
| `EverTold_Asthma` | 1 | Yes |
| | 2 | No |
| `StillHave_Asthma` | 1 | Yes |
| | 2 | No |
| `AsthmaEpisode_Last12Months` | 1 | Yes |
| | 2 | No |
| `EverTold_Arthritis` | 1 | Yes |
| | 2 | No |
| `EverTold_CongestiveHeartFailure` | 1 | Yes |
| | 2 | No |
| `EverTold_CoronaryHeartDisease` | 1 | Yes |
| | 2 | No |
| `EverTold_HeartAttack` | 1 | Yes |
| | 2 | No |
| `EverTold_Stroke` | 1 | Yes |
| | 2 | No |
| `EverTold_COPD` | 1 | Yes |
| | 2 | No |
| `EverTold_Cancer` | 1 | Yes |
| | 2 | No |
| `EverTold_LiverCondition` | 1 | Yes |
| | 2 | No |
| `EverTold_ThyroidProblem` | 1 | Yes |
| | 2 | No |

---

### 19. MENTAL HEALTH - DEPRESSION SCREENER (`mental_health_depression_screener.csv`)
**Purpose:** PHQ-9 Depression Screening

| Variable | Values | Meaning |
|----------|--------|---------|
| `InterestProblemsFrequency_2weeks` | 0 | Not at all |
| | 1 | Several days |
| | 2 | More than half the days |
| | 3 | Nearly every day |
| `DepressionFeelingsFrequency_2weeks` | 0-3 | Same as above |
| `SleepProblemsFrequency_2weeks` | 0-3 | Same as above |
| `FatigueFrequency_2weeks` | 0-3 | Same as above |
| `AppetiteChangesFrequency_2weeks` | 0-3 | Same as above |
| `SelfEsteemIssuesFrequency_2weeks` | 0-3 | Same as above |
| `ConcentrationProblemsFrequency_2weeks` | 0-3 | Same as above |
| `MovementSpeechIssuesFrequency_2weeks` | 0-3 | Same as above |
| `SuicidalThoughtsFrequency_2weeks` | 0-3 | Same as above |
| `DifficultyInFunctioningStatus` | 1 | Not difficult at all |
| | 2 | Somewhat difficult |
| | 3 | Very difficult |
| | 4 | Extremely difficult |

**PHQ-9 Scoring:**
- Sum all 9 items (0-27 total)
- 0-4: Minimal depression
- 5-9: Mild depression
- 10-14: Moderate depression
- 15-19: Moderately severe depression
- 20-27: Severe depression

---

### 20. OCCUPATION (`occupation.csv`)
**Purpose:** Employment status and work patterns

| Variable | Values | Meaning |
|----------|--------|---------|
| `WorkExperience_LastWeek` | 1 | Working at a job/business |
| | 2 | With job, not at work |
| | 3 | Looking for work |
| | 4 | Not working, not looking |
| `HoursWorked_LastWeek` | continuous | Number of hours |
| `UsuallyWorks35HoursOrMore` | 1 | Yes |
| | 2 | No |
| `DaysWorkingPerWeek` | continuous | Number of days (1-7) |
| `MainReasonNotWorking_LastWeek` | 1 | Taking care of house/family |
| | 2 | Unable to work for health reasons |
| | 3 | In school |
| | 4 | Retired |
| | 5 | Other |

---

### 21. ORAL HEALTH (`oral_health.csv`)
**Purpose:** Dental health and issues

| Variable | Values | Meaning |
|----------|--------|---------|
| `MouthPain_Frequency_LastYear` | 1 | Very often |
| | 2 | Fairly often |
| | 3 | Occasionally |
| | 4 | Hardly ever |
| | 5 | Never |
| `LifeSatisfaction_Impact_TeethIssues` | 1-5 | Same frequency scale |
| `DiscomfortEating_TeethIssues` | 1-5 | Same frequency scale |
| `SelfConscious_TeethIssues` | 1-5 | Same frequency scale |
| `OverallHealth_TeethAndGums` | 1 | Excellent |
| | 2 | Very good |
| | 3 | Good |
| | 4 | Fair |
| | 5 | Poor |

---

### 22. PESTICIDE USE (`pesticide_use.csv`)
**Purpose:** Exposure to pesticides

| Variable | Values | Meaning |
|----------|--------|---------|
| `ChemicalProductsUsedInHomeForPestControl` | 1 | Yes |
| | 2 | No |
| `ChemicalProductsUsedInLawnGarden` | 1 | Yes |
| | 2 | No |

---

### 23. PHYSICAL ACTIVITY (`physical_activity.csv`)
**Purpose:** Exercise and sedentary behavior

| Variable | Values | Meaning |
|----------|--------|---------|
| `Frequency_ModerateActivity` | 1-7 | Days per week |
| | 8+ | Special codes for frequency ranges |
| `Duration_ModerateActivity_PerSession` | continuous | Minutes |
| `Frequency_VigorousActivity` | 1-7 | Days per week |
| `Duration_VigorousActivity_PerSession` | continuous | Minutes |
| `SittingTime_TypicalDay` | continuous | Minutes or hours |

---

### 24. PHYSICAL ACTIVITY - YOUTH (`physical_activity_youth.csv`)
**Purpose:** Youth physical activity patterns

| Variable | Values | Meaning |
|----------|--------|---------|
| `Days_PhysicallyActive_AtLeast60Min_Last7Days` | 0-7 | Number of days |
| `ScreenTime_TypicalDay_SchoolYear` | continuous | Hours per day |

---

### 25. PRESCRIPTION MEDICATIONS (`prescription_medications.csv`)
**Purpose:** Medication use

| Variable | Values | Meaning |
|----------|--------|---------|
| `PrescriptionMedication_Used_Last30Days` | 1 | Yes |
| | 2 | No |
| `PrescriptionMeds_Count_Last30Days` | 1 | 1 medication |
| | 2 | 2-4 medications |
| | 3 | 5 or more medications |

---

### 26. PREVENTIVE ASPIRIN USE (`preventive_aspirin_use.csv`)
**Purpose:** Aspirin for cardiovascular prevention

| Variable | Values | Meaning |
|----------|--------|---------|
| `EverTold_TakeAspirin` | 1 | Yes |
| | 2 | No |
| `Following_AspirinAdvice` | 1 | Yes |
| | 2 | No |
| `TakingAspirinOnOwn` | 1 | Yes |
| | 2 | No |

---

### 27. SLEEP DISORDERS (`sleep_disorders.csv`)
**Purpose:** Sleep duration and patterns

| Variable | Values | Meaning |
|----------|--------|---------|
| `WeekdaySleepHours` | continuous | Hours (e.g., 7.5) |
| `WeekendSleepHours` | continuous | Hours (e.g., 8.0) |
| `WeekdaySleepTime` | time | HH:MM format |
| `WeekdayWakeTime` | time | HH:MM format |
| `WeekendSleepTime` | time | HH:MM format |
| `WeekendWakeTime` | time | HH:MM format |


---

### 28. SMOKING - CIGARETTE USE (`smoking_cigarette_use.csv`)
**Purpose:** Cigarette smoking history and current use

| Variable | Values | Meaning |
|----------|--------|---------|
| `SmokedAtLeast100CigarettesInLife` | 1 | Yes |
| | 2 | No |
| `CurrentCigaretteSmoking` | 1 | Every day |
| | 2 | Some days |
| | 3 | Not at all |
| `SmokingTypeMenthol` | 1 | Menthol |
| | 2 | Non-menthol |
| `FirstCigaretteAge` | continuous | Age in years |
| `CigarettesSmokedDays_30Days` | 0-30 | Number of days |
| `CigarettesPerDayOnSmokingDays_30Days` | continuous | Average number |

---

### 29. SMOKING - HOUSEHOLD SMOKERS (`smoking_household_smokers.csv`)
**Purpose:** Secondhand smoke exposure

| Variable | Values | Meaning |
|----------|--------|---------|
| `NumberOfPeopleSmokingInHome` | continuous | Count |
| `NumberOfPeopleSmokingInsideHome` | continuous | Count |

---

### 30. SMOKING - RECENT TOBACCO USE (`smoking_recent_tobacco_use.csv`)
**Purpose:** Recent tobacco and e-cigarette use

| Variable | Values | Meaning |
|----------|--------|---------|
| `UsedAnyTobaccoProduct_5Days` | 1 | Yes |
| | 2 | No |
| `DaysSmokedCigarettes_5Days` | 0-5 | Number of days |
| `CigarettesSmokedPerSmokingDay_5Days` | continuous | Average number |
| `UsedECigarettes_5Days` | 1 | Yes |
| | 2 | No |
| `NumberOfDaysUsedECigarettes_5Days` | 0-5 | Number of days |
| `UsedSmokelessTobacco_5Days` | 1 | Yes |
| | 2 | No |
| `UsedNicotineReplacement_5Days` | 1 | Yes |
| | 2 | No |

---

### 31. WEIGHT HISTORY (`weight_history.csv`)
**Purpose:** Weight status and weight management

| Variable | Values | Meaning |
|----------|--------|---------|
| `CurrentHeight` | continuous | Inches or cm |
| `CurrentWeight` | continuous | Pounds or kg |
| `WeightOneYearAgo` | continuous | Pounds or kg |
| `TriedToLoseWeight_Past12Months` | 1 | Yes |
| | 2 | No |

---

## Data Quality Notes

### Missing Data Patterns
- **Empty cells**: Question was skipped due to survey logic (e.g., pregnancy questions for males)
- **7 = Refused**: Participant declined to answer
- **9 = Don't know**: Participant unsure of answer
- **Very small numbers** (e.g., 5.397605346934028e-79): May represent special missing codes

### Special Considerations
1. **Skip patterns**: Many questions only asked if previous answers meet criteria
2. **Age restrictions**: Some questionnaires only for certain age groups
3. **Proxy responses**: Some data from family members for young children
4. **Survey weights**: Available for population-representative estimates (not included in these simplified files)

---

## Resources

- **Official NHANES Website**: https://wwwn.cdc.gov/nchs/nhanes/
- **NHANES Tutorials**: https://wwwn.cdc.gov/nchs/nhanes/tutorials/default.aspx
- **Variable Search**: https://wwwn.cdc.gov/nchs/nhanes/search/
- **Questionnaires**: Available on NHANES website by cycle and component

---

## Citation

When using this data, cite:
> Centers for Disease Control and Prevention (CDC). National Center for Health Statistics (NCHS). National Health and Nutrition Examination Survey Data. Hyattsville, MD: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, 2021-2023. https://wwwn.cdc.gov/nchs/nhanes/

---

*Last Updated: November 12, 2025*
*Dataset: NHANES 2021-2023 Cycle*
