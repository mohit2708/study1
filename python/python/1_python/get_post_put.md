### POST और PUT का Difference (Hindi में समझिए)
#### POST Method
- **काम:** नया data / नया record बनाना
- Idempotent नहीं होता (बार-बार call करने पर नया-नया record बनेगा)
- URL server decide करता है
- ज़्यादातर form submit या new user create करने में use होता है
- हर बार call करने पर नया user बनेगा

#### PUT Method
- **काम:** पहले से मौजूद data को update / replace करना
- Idempotent होता है (कितनी भी बार call करो, result same रहेगा)
- URL client देता है
- ज़्यादातर complete record update करने में use होता है

### PUT और PATCH का Difference (Hindi में)
#### PUT Method
- **काम:** पूरा record replace करना
- पूरा data भेजना जरूरी होता है
- Idempotent होता है
- अगर कोई field miss हो जाए, तो वह field null / delete हो सकती है

#### PATCH Method
- **काम:** record का partial update करना
- सिर्फ वही fields भेजते हैं जो बदलनी हों
- आमतौर पर Idempotent माना जाता है
- बाकी data पर कोई असर नहीं पड़ता
