# Bad-Apple-ASCII-Art
Background  
  Bad Apple is a song composed by ZUN, creator of the Touhou Series. Touhou Series is a game series starting since 1997 which features 19 main-line games and 13 spin offs where ZUN did all of the music composition, graphic art, writing, and coding all on his own. Bad Apple is a song which was originally featured in Touhou 4, lotus land story(https://www.youtube.com/watch?v=w7IoHiD0Kuo). Zun allows for free use of all of his Touhou Franchise as long as it follows some rules and conditions, this has allowed for remixing of his music, and free use of the characters he has designed in the Touhou Series. Thanks to this decision by ZUN, his works have given birth to the Touhou Project, which involves fans using the base foundation of music and characters in the Touhou Series to create their own games, animations, remixs, manga, and songs. Notable songs in the Touhou Series include but are not limited to U.N owen was her, necrofantasia, Night of Nights, We are Japanese goblins, tiny little adiantum, and Marisa Stole the Precious Thing. Thanks to the freedom given by ZUN, Bad Apple was able to be remixed by Alstroemeria Records and provided lyrics sung by Nomico in 2007 and later a follow up animation by NICONICODOUGA user "Anira" to form what Bad Apple is known as today.

This Project is heavily inspired by youtuber Junferno(https://www.youtube.com/@Junferno/videos : https://github.com/kevinjycui)



Final Project Video

https://www.youtube.com/watch?v=Xpw_-MhCeLc&feature=youtu.be 


The difficulties I faced in this project was mainly trying to sync up my audio with my visuals and having those things match up with the actual music video itself. Since setting the "sleep" delay to 1/30 didn't actually mean I was setting my animation to 30 frames per second for whatever reason, I had to manually find out which speed works best and that took hours of trial and error. 

Others issue would be having to do the research to get everything to work and finding out what useful imports there were. 
Examples would be "from natsort import natsorted". Since my images weren't listed out as 0001 and 0010 ect, the images would play out of order in the for loop because python reads in the order of the first number, so 100 would come before 2 if its not written as 002.
I also had issues with playing my audio because things are processed in order when you run a code. So if my audio file came before my images the entirety of the song would play out before the images. "winsound.SND_ASYNC" was able to fix this issue by playing both simultaneously

Overall I learned a lot from this project, I was able to realize the process of making ASCII art and how simple it was overall. But I needed to figure out how to read image files and how to store it in a for loop in order to print everything in the right order and correctly. Thanks to these processes I realized just how useful the imports of python are, without these imports I would have had to do everything from scratch, like greyscaling the images on my own. 

This was a complete passion project as I have loved the Touhou Franchise for so long, especially Bad Apple was a huge obssession of mine. So being able to recreate it using ASCII art was a ton of fun. 
