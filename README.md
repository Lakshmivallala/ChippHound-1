# ChippHound
> Smart Surveillance System

At present, a lot of labour is spent on physical patrolling of border areas, cities and compounds. Fencing wires or barricades are not reliable and easy to breach, in large areas it is difficult to be available at all locations, and if someone is breaching in absence of guard, the guard will know only when they reach the breach site. Also, it takes a lot of time to cover the compound walls if the area is large. For smarter India, we need a Smarter Surveillance system, which can be developed through Modular design which is easy to assemble at onsite.


## Solution
- Our application detects human-presence through a model which is pre-trained weights of Single Shot Multibox Detector with MobileNet dataset. It can be used to detect various objects but we limited it to humans. 
- However, the algorithm cannot detect objects under low light conditions because there is not enough exposure to identify the shape of the contents. We used methods like automatic gamma adjustments and light intensity correction to tackle this problem and results turned out to be amazing.
- We used AWS Rekognition with pre-trained models to detect violence like physical voilence, sexual violence, weapon violence, nudity and gore, etc.
- As soon the application detects the intrusion/violence it sends an alert email to the authorities with a snapshot of that feed which makes it easier to identify the situation and act accordingly.
- Our application sends Telegram messages with a snapshot attached, it also makes automated phone calls and SMSs alerting the authorities.

### Raspberry Pi
We used Raspberry Pi as our main platform for this project due to the following reasons.
- Very Compact
- Low Cost
- Portable
- Efficient 
- Can connect to devices wirelessly
