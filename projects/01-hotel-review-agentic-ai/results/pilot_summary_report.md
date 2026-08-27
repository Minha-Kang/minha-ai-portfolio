# clean_hotel Pilot 1, 2 strict version report

## Data
- Project dir: `/content/drive/MyDrive/Portfolio/hotel`
- Dataset path: `/content/drive/MyDrive/Portfolio/hotel/clean_hotel`
- Selected reviews: 10

## Selected reviews
- G01 | train:6371 | rating=1 | words=2140 | title=Filthy deluxe room, great suite, but service is almost non-existence
- G02 | train:2909 | rating=1 | words=1022 | title=Repeat customer.... But not any more!
- G03 | train:6344 | rating=2 | words=1085 | title=Fools Gold would be the best way to describe Hotel Michael
- G04 | train:5669 | rating=2 | words=989 | title=Stay somewhere else if you have a choice.
- G05 | train:900 | rating=3 | words=2037 | title=Good Hotel in Many Ways, But Some Inconsiderate Guests and Appalling Booking Service with 
- G06 | train:6779 | rating=3 | words=1301 | title=Great location, but...
- G07 | train:15739 | rating=4 | words=2687 | title=This is a chalet/ranch style place. Value for money not for high end.
- G08 | train:12474 | rating=4 | words=1409 | title=A Very Unusual Hotel that's Not for Everyone (But a Great Spot for the Right Clientele)
- G09 | train:13171 | rating=5 | words=1347 | title=Excellent, 5-star review, with nothing to complain about
- G10 | train:15120 | rating=5 | words=1072 | title=HGI Singapore = Great Hilton Hotel.  We will be back.

## Pilot 1
- Context–Aspect–Event rows: 98
- Unique actionable issues: 50
- Max mention_count: 4
- Failure Score = review-level mention_count × negative_ratio × avg_intensity

Top failure issues:
- C3_RoomStay | Cleanliness | dirty_or_stained | mention=4 | score=7.43 | evidence=bedsheets are dirty, covering with stains || 4 pillows had stains || curtains ... filled with stain marks
- C3_RoomStay | Bathroom | bathroom_design_issue | mention=4 | score=6.00 | evidence=shower curtain did not hang low enough || Shower & toilet are tiny || sliding door with no lock or hook
- C2_Arrival_Checkin | Staff_Service | staff_unfriendly_rude | mention=3 | score=6.00 | evidence=lady at the counter does not seem to be interested || unwelcoming, as if we were an inconvenience || no help, no apology
- C4_FacilityUse | Facility | facility_negative | mention=4 | score=4.80 | evidence=generator was extremely noisy || gym ... squeezing in the tiny area || only 4 beach chairs
- C6_Complaint_StaffResponse | Service_Recovery | service_failure | mention=2 | score=4.00 | evidence=Not one single phone call from the desk || guest services actually called me to try to bill me an additional amount

## Pilot 2
- Single LLM prediction rows: 98
- LLM-SQE final prediction rows: 98

Verifier counts:
- pass: 95
- fail: 3

Weak gold comparison is reference-only because clean_hotel labels are review-level weak labels, not sentence/evidence-level gold labels.

Weak gold summary:
- llm_sqe_final: n=48, MAE=0.646, RMSE=0.924, sign_acc=0.792
- single_llm: n=42, MAE=0.929, RMSE=1.123, sign_acc=0.690

## Private mini-gold
- Gold labels are not embedded in this notebook.
- Fill template: `/content/drive/MyDrive/Portfolio/hotel/pilot_outputs_clean_hotel_strict/00_private_mini_gold_template_FILL_MANUALLY.csv`
- Optional private gold path: `/content/drive/MyDrive/Portfolio/hotel/private/private_mini_gold_10.csv`