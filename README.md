Welcome to Metin Ulaş Erdoğan's self analysis of spotify listening history.

First let's begin with the reason why I decided to use my spotify data.
To be honest it has nothing to do with homework 1. i don't use traditional social media. i have a reddit account wheree i delete search history often, have my youtube history turned off, no insta, not twitter (or x) etc.
the ones i could use are my bank transactions, google maps data, discord chat log, spotify streaming history, and steam data.
as you can imagine i didn't want to use the first 2 from the beginning so i tried to request my data from the latter 3.
so i used my right to request my data from the service providers thanks to UN's law set in 2018. (check General Data Protection Regulation if you want more info) and requested my personal data from spotify and discord.
i haven't requested data from steam because it was more of a hassle to request, compared to pressing a couple buttons.
then i checked the data i got from both those platforms and decided that using my discord chat logs beginning from 2017 would be a nightmare for both me and the reader so i stick with spotify data. which was around the time of homework's release.

spotify sent me data in 3 batches, one of them was about the technical information, which included some hard to make sense data. the most i could use to make sense was how much battery my device haad at the given time. As you may guess i didn't use it as well.
the other batch was the not so detailed batch. it included up to 2 years old data (i think? it was nowhere near 2018 data at least) and it didn't have any details. it had the info of the track name, track artist name, and when it was listened.
this data was obviously not enough and not usable in making api calls to get more data as well.

but after that i checked the data from extended history files. Those were quite detailed actually. here is a sample of it

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/41743d5e-c4a9-4ccb-98ee-c42711f95449)
this is only 1 sample of the tracks (which i quite like, would recommend you to listen, here is a url for it ---> https://open.spotify.com/intl-tr/track/3aam0kEa1rs9Zk1X0V2QC6?si=ab1a816e30394737)

there were 7-8 files including such json entries listed.

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/c0af96ca-384a-4d25-b919-b523262ff045)

for your interest a json file's length varies around 350 to 400 thousand lines
and this data was not detailed enough for me to use. but before requesting some extra data i needed to filter my tracks.

at this point i came up with some criterias to filter the songs i listened.
the data had the songs i skipped right after i started playing them. so i had to decide which songs i was supposed to analyze.
for that i have written Data_Filter.py which you can find in this repo.
basically what it does is if a song is not on spotify anymore (which i can't request their detailed data anymore) and the song was played more than 45 seconds i will add this song to my samples.
here is the code for it

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/1d96781e-9d0d-4294-b95c-24b3538559c5)
and here is the sample outputs from that file

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/71444822-b360-4375-8cba-e59e5bc41bba)

at this point i could start working on getting the song analysis of each track in my new samples. for this i was going to use spotify web api.
i spent some of my time doing some other projects using spotify web api in this semester. By the help of that experiments i learned how i can request the details the tracks had on homework 1 so i might use them.


