"""
Run to generate well formatted (not necessarily grammatical) filler sentences from Kush 2013.
There was a small consistency error with the first curly brace option in both datasets. 
Beyond this small fix, all other sentences are taken directly from Kush 2013
"""

experiment_4 = """
1. Jane asked which {maintenance man/lunch lady} {it appeared / had said } that {he
/Donna} might have already spoken with regarding the food-fight in the cafeteria.
2. Lily wondered {which tailor/seamstress} {it seemed/ had said} that {he /Alice}
could have recently called on for sewing assistance before the wedding.
3. Mary knew which {policeman/policewoman} {it appeared/had admitted} that {he
/Hailey} should have immediately talked to after the accident on the highway.
4. Christina remembered {which fireman/mother} {it seemed/had admitted} that {he
/Diane} should have immediately reported to after the catastrophe in the city.
5. Olivia said which {doctor/midwife} {it appeared/had thought} that {he /Kaitlyn}
might have already spoken with about the prognosis for good recovery.
6. Jessica asked which {cowboy/cowgirl} {it seemed/had thought} that {he /Theresa}
should have actually fought with during the cattle-drive on the ranch.
7. Ashley wondered which {gangster/prostitute} {it appeared/had said} that {he /Su-
sanne} should have probably gone after in the alleyway during the sting.
8. Emily knew which {judge/typist} {it seemed/had said} that {he /Eve} must have
actually disagreed with about the ruling by the court.
9. Sarah remembered which {monk/nun} {it appeared/had confessed} that {he /Nora}
might have privately talked to in the rectory after the mass.
10. Megan said which {engineer/secretary} {it seemed/had admitted} that {he /Chris-
tine} might have actually agreed with about the blueprints for the skyscraper.
11. Hannah couldn’t remember which {boy/girl} scout {it appeared/had implied} that
{he /Bridget} would have gone fishing with on troop trips in the summers.
12. Lauren couldn’t remember which {soldier/nurse} {it seemed/had disclosed} that
{he /Catherine} might have secretly conspired with to steal provisions from the
infirmary.
13. Michael asked which {stripper/bouncer} {it appeared/had said} that {she /Omar}
should have immediately looked for outside the club after last call.
14. Christopher wondered which {aunt/uncle} {it appeared/had said} that {she /Felix}
could have easily corresponded with according to staff at the retirement home.
15. Matthew knew which {nanny/boy} {it seemed/had claimed} that {she /Jorge} would
get stuck waiting for during afternoon dismissal outside the school.
16. Joshua remembered which {princess/prince} {it appeared/had said} that {she
/Brian} would have discreetly taken aside during the ball to discuss rumors.
17. Jacob found out which {maid/butler} {it seemed/had insisted} that {she /Brad}
would have gladly spied on during the lunch-break for the investigators.
18. Nick asked which {sorority girl/frat boy} {it appeared/had thought} that {she
/Mandy} would have definitely bumped into at the mixer during welcome week.
19. Andrew wondered which {receptionist/dentist} {it seemed/had said} that {she
/Peter} could have already spoken to about the benefits of dental insurance.
20. Daniel knew which {waitress/waiter} {it appeared/had complained} that {she /Tina}
must have already worked with during dinner rush on Tuesday night.
21. Tyler remembered which {nurse/doctor} {it seemed/had believed that} {she /Eileen}
should have immediately talked to after the outbreak in the ward.
22. Joseph said which {secretary/executive} {it appeared/had conceded} that {she
/Howard} should have frequently consulted with with the typing of the reports.
23. Brandon couldn’t recall which {nun/priest} {it seemed/had thought} that {she /Paul}
might have actually talked with about the interpretation of the scripture.
24. David couldn’t recall which {girl/boy} scout {it appeared/had believed} that {she
/Jeff} could have actually worked with during the fundraiser for new uniforms.
25. Mary asked which {knight/baroness} {it appeared/had declared} that {he /Evelyn}
would have valiantly fought for during the joust at the fair.
26. Sam described which {bride/groom} {it seemed/had insisted} that {she /Andrew}
would have never waited for before the dress-fitting at the store.
27. Eliza questioned which {bully/girl} {it seemed/had said} that {he /Harry} might
have been hiding from behind the slide on the playground.
28. Sean asked which {ballerina/boxer} {it appeared/had thought} that {she /Samantha}
could have actually tied with in the exhibition at the gym.
29. Rosie knew which {linebacker/cheerleader} {it appeared/had said} that {he /Shelly}
would have rather spoken with for the article in the newspaper.
30. Adam recalled which {actress/actor} {it seemed/had implied} that {she /Ellen}
would have rather studied under in the workshops at the conservatory.
31. Angela mentioned which {professor/kindergarten teacher} it {seemed/had} claimed
that {he /Melanie} would have formally written up for teaching evolution to the
class.
32. Benjamin described which {salesgirl/salesman} {it appeared/had claimed} that {she
/Richard} would have angrily yelled at for the faulty merchandise in stock.
33. Ingrid reported which {emperor/empress} {it appeared / had implied} that {he
/Isabel} might have secretly conspired with to plan imprisoning many local revolu-
tionaries.
34. Allan forgot which {sorceress/sorcerer} {it seemed/had admitted} that {she /Kevin}
would have gladly fought against during the battle in the novel.
35. Leah didn’t know which {farmer/milkmaid} {it seemed/had said} that {he /Carolyn}
might have accidentally ripped off at the market on Sunday afternoon.
36. Jack reported which {policewoman/policeman} {it appeared/had admitted} that
{she /Eric} might have unintentionally shot at in the basement during the firefight.
"""

experiment_5 = """
1. Jane asked which {maintenance man/lunch lady} {it appeared / had said } that {his
supervisor/Donna} might have already spoken with regarding the food-fight in the
cafeteria.
2. Lily wondered which {tailor/seamstress} {it seemed/ had said} that {his appren-
tice/Alice} could have recently called on for sewing assistance before the wedding.
3. Mary knew which {policeman/policewoman} {it appeared/had admitted} that {his
partner/Hailey} should have immediately talked to after the accident on the highway.
4. Christina remembered {which fireman/mother} {it seemed/had admitted} that {his
buddy/Diane} should have immediately reported to after the catastrophe in the city.
5. Olivia said which {doctor/midwife} {it appeared/had thought} that {his asso-
ciate/Kaitlyn} might have already spoken with about the prognosis for good re-
covery.
6. Jessica asked which {cowboy/cowgirl} {it seemed/had thought} that {his em-
ployer/Theresa} should have actually fought with during the cattle-drive on the
ranch.
7. Ashley wondered which {gangster/prostitute} {it appeared/had said} that {his ri-
val/Susanne} should have probably gone after in the alleyway during the sting.
8. Emily knew which {judge/typist} {it seemed/had said} that {his colleague/Eve}
must have actually disagreed with about the ruling by the court.
9. Sarah remembered which {monk/nun} {it appeared/had confessed} that {his ab-
bott/Nora} might have privately talked to in the rectory after the mass.
10. Megan said which {engineer/secretary} {it seemed/had admitted} that {his man-
ager/Christine} might have actually agreed with about the blueprints for the skyscraper.
11. Hannah couldn’t remember which {boy/girl} scout {it appeared/had implied} that
{his leader/Bridget} would have gone fishing with on troop trips in the summers.
12. Lauren couldn’t remember which {soldier/nurse} {it seemed/had disclosed} that
{his sergeant/Catherine} might have secretly conspired with to steal provisions from
the infirmary.
13. Michael asked which {stripper/bouncer} {it appeared/had said} that {her admirer/Omar}
should have immediately looked for outside the club after last call.
14. Christopher wondered which {aunt/uncle} {it appeared/had said} that {her nephew/Felix}
could have easily corresponded with according to staff at the retirement home.
15. Matthew knew which {nanny/boy} {it seemed/had claimed} that her {employer/Jorge}
would get stuck waiting for during afternoon dismissal outside the school.
16. Joshua remembered which {princess/prince} {it appeared/had said} that {her advi-
sor/Brian} would have discreetly taken aside during the ball to discuss rumors.
17. Jacob found out which {maid/butler} {it seemed/had insisted} that {her supervi-
sor/Brad} would have gladly spied on during the lunch-break for the investigators.
18. Nick asked which {sorority girl/frat boy} {it appeared/had thought} that {her sis-
ters/Mandy} would have definitely bumped into at the mixer during welcome week.
19. Andrew wondered which {receptionist/dentist} {it seemed/had said} that {her man-
ager/Peter} could have already spoken to about the benefits of dental insurance.
20. Daniel knew which {waitress/waiter} {it appeared/had complained} that {her
friend/Tina} must have already worked with during dinner rush on Tuesday night.
21. Tyler remembered which {nurse/doctor} {it seemed/had believed that} {her pa-
tient/Eileen} should have immediately talked to after the outbreak in the ward.
22. Joseph said which {secretary/executive} {it appeared/had conceded} that {her
boss/Howard} should have frequently consulted with with the typing of the reports.
23. Brandon couldn’t recall which {nun/priest} {it seemed/had thought} that {her
priest/Paul} might have actually talked with about the interpretation of the scripture.
24. David couldn’t recall which {girl/boy} scout {it appeared/had believed} that {her
mother/Jeff} could have actually worked with during the fundraiser for new uni-
forms.
25. Mary asked which {knight/baroness} {it appeared/had declared} that {his compatri-
ots/Evelyn} would have valiantly fought for during the joust at the fair.
26. Sam described which {bride/groom} {it seemed/had insisted} that {her girlfriends/Andrew}
would have never waited for before the dress-fitting at the store.
27. Eliza questioned which {bully/girl} {it seemed/had said} that {his victim/Harry}
might have been hiding from behind the slide on the playground.
28. Sean asked which {ballerina/boxer} {it appeared/had thought} that {her rival/Samantha}
could have actually tied with in the exhibition at the gym.
29. Rosie knew which {linebacker/cheerleader} {it appeared/had said} that {his inter-
viewer/Shelly} would have rather spoken with for the article in the newspaper.
30. Adam recalled which {actress/actor} {it seemed/had implied} that {her replace-
ment/Ellen} would have rather studied under in the workshops at the conservatory.
31. Angela mentioned which {professor/kindergarten teacher} it {seemed/had} claimed
that {his student/Melanie} would have formally written up for teaching evolution to
the class.
32. Benjamin described which {salesgirl/salesman} {it appeared/had claimed} that {her
client/Richard} would have angrily yelled at for the faulty merchandise in stock.
33. Ingrid reported which {emperor/empress} {it appeared / had implied} that {his
advisors/Isabel} might have secretly conspired with to plan imprisoning many local
revolutionaries.
34. Allan forgot which {sorceress/sorcerer} {it seemed/had admitted} that {her ene-
mies/Kevin} would have gladly fought against during the battle in the novel.
35. Leah didn’t know which {farmer/milkmaid} {it seemed/had said} that {his helpers/Carolyn}
might have accidentally ripped off at the market on Sunday afternoon.
36. Jack reported which {policewoman/policeman} {it appeared/had admitted} that
{her back-up/Eric} might have unintentionally shot at in the basement during the
firefight.
""" 

import re
import itertools
import json

def process_sentences(raw):
    """
    Takes the raw sentences above and returns all possible sentence options
    """
    sentences = []
    raw = raw.replace("-\n", "")
    raw = raw.replace("\n", " ")
    raw = raw.replace("’", "'")
    raw_sentences = re.split(r"\d+\. ", raw)
    for raw_sentence in raw_sentences[1:]:
        choices = re.findall(r"{(.*?)/(.*?)}", raw_sentence)
        choices_products = list(itertools.product(*choices))
        group_sentences = []
        for words in choices_products:
            sentence = re.sub(r"{(.*?)/(.*?)}", "{}", raw_sentence)
            group_sentences.append(sentence.format(*words).replace("  ", " ").strip())
        sentences.append(group_sentences)
    return sentences

json.dump(process_sentences(experiment_4), open("data/kush_2013_experiment_4_strong_crossover.json", "w"), indent=4)
json.dump(process_sentences(experiment_5), open("data/kush_2013_experiment_5_weak_crossover.json", "w"), indent=4)

