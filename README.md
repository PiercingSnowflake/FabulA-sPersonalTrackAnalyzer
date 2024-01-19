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

at this point i got a bit curious about how many days of my life i've spent listening to music so i've written main.py

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/def5de37-5d21-45cf-b6f4-4b554f51257f)

and it turns out i've spent 230 days since 2018. and there is a time where i reduced spotify usage as i was also using youtube music. Remember that this only includes the filtered songs so it is actually quite longer.


at this point i could start working on getting the song analysis of each track in my new samples. for this i was going to use spotify web api.
i spent some of my time doing some other projects using spotify web api in this semester. By the help of that experiments i learned how i can request the details the tracks had on homework 1 so i might use them.
after that i created such an app

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/e1e94e62-70c9-4eeb-849a-0462f81532ef)

the monthly active users are quite low (0) as i don't have any more use of this app.
but if you want to use spotify web api here's a link for you ---> https://developer.spotify.com/

anyways, to return to subject i've used the app with these files

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/6c514973-eb34-4819-a88b-f017f4ccc78d)

i can't send the code in a ssingle screenshot as it is larger than that yet you can see the code in the repository
as for the json files' structure they are like this

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/7dbc4f6e-089d-4449-ac3a-56f876d9f6b3)

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/4bb37540-5293-4e2d-b3d4-c0d6277357d9)

Using these tokens i requested the audio features of the songs in my new filtered dataset via the code in Absolute_Data_Collector.py yet this process was quite difficult.
Because spotify web api allows me to send a limited number of requests per time interval. and as from my experience the time you need to wait after reaching the request limit is not some 1 hour waiting but posssibly 12 hours, possibly a day. maybe it can have a reset at a given time of the day i don't know. Yet my data was so big that i kept hitting this wall so i needed a way to walk around it.
i already expected such a thing happening so i sent requests in batches of 100 tracks per request yet it still was quite long

here is the solution i found.
from some experience i knew that i could request around 60-70% of the data so i splitted my data into 2 with the help of the code Filtered_Splitter.py

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/5be8ff63-0c70-4441-a404-5b8a49f27983)

as far as i remember this code had a slight isssue of arranging the [] paranthesis at the beginning and the end of the file so i had to fix them manually. it took less than a minute to fix anyways.

Then i ran the code to get audio features from endpoint audio_features_url = 'https://api.spotify.com/v1/audio-features' once again (the absolute data collector file)

then i thought i got all the tracks' audio features and was happy for 1-2 days. Only to realize that i got "scammed" by spotify.

the new issue is this
let's create a batch of 100 tracks i listened.
let's say i had such a listening queue

Aerie & Howling
20 Years of Dysphoria and a Half-Entropy
rosa centifolia
Chlo\u00e9
Le Porteur d'Ombre
escape (the looking-glass, and what alice found there)
Solstice
rosa centifolia
Aerie & Howling
20 Years of Dysphoria and a Half-Entropy


as these are in the same batch of 100 songs which were sent to spotify in the request, spotify api did a lazy work and only gave me the audio features of the first instances of the tracks.
like the first json object for the Aerie & Howling has the audio features i requested. yet the 2nd one doesn't have it. but somewhere later in the file it still has the audio features.

Also i'm talking about audio features but to give example they are those values we worked on homework 1

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/aa19384d-4616-45d0-b958-dcd95e53b818)

you can wonder that where is the genres of the tracks? they are not associated with the tracks but associated with the artists. so this project doesn't have the genres. I still could add them but i didn't because of a couple reasons. 1st is that i was lazy, 2nd is if i was going to do it it would cost me more api requests. 3rd is that fixing of the dataset was almost driving me mad due to this last issue i explained and the same thing was going to happen again. 4th reason is that the project was already going to post the most frequent artists and stuff which i could show. and the 5th reason is that i have many artists which i listen to marked with the genre as "rythm games" which is not a genre at all. i couldn't just say the neurofunk track, the speedcore one and the electornica one are all rythm games. it just wouldn't make sense.

anyways, to return to the subject. i had to fix the isssue of the lacking datas. so i've written the missing_data_filler.py which was a nice try at best. then i realized that i forgot to add the artist names to my data at the data_filter.py step, the one with 45 second threshold and the song must still be in spotify one.

then i wrote the code forgot_to_add_artist_names_cuz_im_dumb.py. which basically finds the artist names by matching them from the initial files spotify sent me with track uris and artist names. once it finds a matching uri between 2 files it adds the artist name of the track and keeps it in a new file.

but somehow some details were still not on this new file. so i wrote another code named result_file_fixer.py which worked fine (finally). what that code done was it was running from the result of the previous file one by one. if it finds a json entry without the audio analysis it gets its uri, the code was running through entire file once again to see if there is a json object with same uri with the audio analysis. once it finds such an object it copies the audio features of that track and pastes it to the object with missing values. I am aware of its time complexity. but i had to find a solution quick, not a quick solution. hence i used this brute force approach.

after that i had my 170 mb of json data file

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/4639dad5-b226-4bb1-ae89-370072b877bc)

afterwards i did work on the data a bit

i've written a code to plot my most listened artists first. which had the result:

![MostListenedArtists](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/8d42b97a-ef15-46f0-941f-ebf7f68587d5)

then i've written another code to show my most listened songs by both the hours i listened them and the times i listened them
here are both their graphs


![mostlistenedsongsbyplaycount](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/e2927705-1128-45aa-8865-7538368d3f48)
![mostlistenedsongsbyhours](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/1071355b-1722-4cd6-9534-3ead04112dd1)

then made an experimental code to see how likely i am to skip a song based on the audio features i've gathered (after 45 seconds, as in skipping in the middle of it)

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/7ee65c3c-25e5-4fae-8d0f-88d4fa196eb4)

it seems i skip the songs quite often

then i followed by using the values which were quite a hassle to gather. i showed how much they changed over the years
![acousticness](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/e2728368-5c15-4920-bef3-c5ea501c9df7)
![energy](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/9e2df184-a243-46c9-a40b-1754dbb90834)
![danceability](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/42df3335-ee9f-4581-a2a4-7b31a539c595)
![valence](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/bac6eede-e9bf-4916-a59b-9cf155980335)

![image](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/335b49fd-c410-44d1-aa13-aebc9ef27ffa)

Spotify uses the word “valence” to measure whether a song is likely to make someone feel happy (higher valence) or sad (lower valence). The metric is measured on a scale from 0.0 to 1.0. "Danceability" refers to how suitable a track is for dancing based on a combination of musical elements. so during the covid19 years it nicely coincides with that value getting lower

other values also show a similar trend. yet the energy value shows the quite opposite one

and finally there is the total listening time and number of songs played graphs over months

![numhoursovermonths](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/7228664a-4ca2-4889-b5c4-f5d7ee10752b)
![numsongovermonths](https://github.com/PiercingSnowflake/FabulA-sPersonalTrackAnalyzer/assets/56087824/b0a056b9-cc0a-44b1-a15d-ac64a8c61ad7)

i can't find much of a seaasonality or a trend on these ones but i can say that i usually listen a lot.



