from django.core.management.base import BaseCommand
from heroes.models import Superhero
from django.core.files import File
import requests
import os
from io import BytesIO
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populates the database with initial superheroes'

    def handle(self, *args, **options):
        # Ensure the media/superhero_main_images directory exists
        media_dir = 'media/superhero_main_images'
        os.makedirs(media_dir, exist_ok=True)
        User = get_user_model()
        try:
            admin_user = User.objects.get(username='prashant')  # Replace 'admin' with your actual admin username if different.
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Admin user not found. Please create an admin user before running this command."))
            return

        superhero_data = [
            {
                "name": "Spider-Man",
                "universe": "Marvel",
                "powers": "Superhuman strength, speed, agility, wall-crawling, spider-sense",
                "first_power": "Wall-Crawling",
                "story": "Bitten by a radioactive spider, Peter Parker gains superpowers and becomes Spider-Man, balancing his heroic duties with his everyday life.",
                    "real_creator": "Stan Lee and Steve Ditko",
                    "movies": "Spider-Man (2002), Spider-Man 2 (2004), Spider-Man 3 (2007), The Amazing Spider-Man (2012), The Amazing Spider-Man 2 (2014), Spider-Man: Homecoming (2017), Spider-Man: Far From Home (2019), Spider-Man: No Way Home (2021)",
                    "shows": "Spider-Man: The Animated Series, The Spectacular Spider-Man, Ultimate Spider-Man",
                    "main_image_url": "https://static.wikia.nocookie.net/spiderman/images/0/08/Spider-Man_%28MCU%29_Profile.jpg",
                    "bio": "Peter Parker, a high school student, gains extraordinary abilities after being bitten by a radioactive spider.  He uses his powers to fight crime and protect the innocent as the amazing Spider-Man, often juggling his superhero life with the challenges of being a teenager and later a young adult.  Known for his quick wit, agility, and sense of responsibility, Spider-Man is a beloved hero who embodies the idea that with great power comes great responsibility.",
                    "alter_ego": "Peter Parker",
                    "base": "New York City",
                    "comic_series": "Amazing Spider-Man, Ultimate Spider-Man, Spectacular Spider-Man",
                    "wisdom": 75,
                    "raw_power": 80,
                    "combat_skills": 90,
                    "durability": 85,
                    "intelligence": 90,
                    "agility": 95
                },
                {
                "name": "Hulk",
                "universe": "Marvel",
                            "powers": "Superhuman strength, durability, regeneration, rage-enhanced power",
                            "first_power": "Superhuman Strength",
                            "story": "Exposed to gamma radiation, scientist Bruce Banner transforms into the Hulk, a rage-fueled monster with incredible strength.",
                            "real_creator": "Stan Lee and Jack Kirby",
                            "movies": "Hulk (2003), The Incredible Hulk (2008), The Avengers (2012), Avengers: Age of Ultron (2015), Thor: Ragnarok (2017), Avengers: Infinity War (2018), Avengers: Endgame (2019)",
                            "shows": "The Incredible Hulk (1978 TV series), Hulk and the Agents of S.M.A.S.H.",
                            "main_image_url": "https://static.wikia.nocookie.net/marveldatabase/images/0/0b/Bruce_Banner_%28Earth-616%29_from_Hulk_Vol_5_1_001.jpg",
                            "bio": "Dr. Bruce Banner, a brilliant physicist, was exposed to high levels of gamma radiation during a military experiment. As a result, whenever he experiences extreme stress or anger, he transforms into the Hulk, a creature of immense strength and rage. The Hulk's power is virtually limitless, increasing with his anger. While often seen as a destructive force, the Hulk has also been a powerful ally to the Avengers and other heroes, using his strength to protect the innocent and fight against evil.",
                            "alter_ego": "Bruce Banner",
                            "base": "None (Nomad)",
                            "comic_series": "The Incredible Hulk",
                            "wisdom": 40, 
                            "raw_power": 100,
                            "combat_skills": 80,
                            "durability": 100,
                            "intelligence": 100,
                            "agility": 70
                },    
                {
                        "name": "Wolverine",
                        "universe": "Marvel",
                        "powers": "Regenerative healing factor, superhuman senses, retractable adamantium claws, superhuman strength, agility, and durability",
                        "first_power": "Healing Factor",
                        "story": "A mutant with a mysterious past, Wolverine's healing abilities and adamantium skeleton make him a formidable warrior.",
                        "real_creator": "Len Wein, John Romita Sr., and Herb Trimpe",
                        "movies": "X-Men (2000), X2 (2003), X-Men: The Last Stand (2006), X-Men Origins: Wolverine (2009), The Wolverine (2013), X-Men: Days of Future Past (2014), X-Men: Apocalypse (2016), Logan (2017)",
                        "shows": "X-Men: The Animated Series, Wolverine and the X-Men",
                        "main_image_url": "https://static.wikia.nocookie.net/xmenmovies/images/4/40/Wolverine.png",
                        "bio": "Wolverine, also known as Logan, is a mutant with an accelerated healing factor, enhanced senses, and retractable adamantium claws. His past is shrouded in mystery, but he has been a member of various X-Men teams, fighting for mutant rights and protecting the world from threats. Wolverine's gruff personality and fierce fighting style make him a complex and compelling character.  His healing ability allows him to survive nearly any injury, and his adamantium claws can cut through almost anything. Despite his rough exterior, Wolverine is deeply loyal to his friends and willing to sacrifice everything to protect them.",
                        "alter_ego": "James Howlett (Logan)",
                        "base": "Xavier's School for Gifted Youngsters",
                        "comic_series": "X-Men, Wolverine, Origin",
                        "wisdom": 80,
                        "raw_power": 85,
                        "combat_skills": 95,
                        "durability": 95,
                        "intelligence": 70,
                        "agility": 90
                    },
                    {
                "name": "Spider-Man",
                "universe": "Marvel",
                "powers": "Superhuman strength, speed, agility, wall-crawling, spider-sense",
                "first_power": "Wall-crawling",
                "story": "Bitten by a radioactive spider, Peter Parker gains extraordinary abilities and becomes Spider-Man.",
                "real_creator": "Stan Lee, Steve Ditko",
                 "movies": "Spider-Man (2002), Spider-Man 2 (2004), Spider-Man 3 (2007), The Amazing Spider-Man (2012), The Amazing Spider-Man 2 (2014), Spider-Man: Homecoming (2017), Spider-Man: Far From Home (2019), Spider-Man: No Way Home (2021),  Across the Spider-Verse (2023)",
                "shows": "Spider-Man: The Animated Series, Spectacular Spider-Man",
                "main_image_url": "https://upload.wikimedia.org/wikipedia/en/2/21/Web_of_Spider-Man_Vol_1_129-1.png",
                  "bio": "Peter Parker, a high school student, gains spider-like abilities after being bitten by a radioactive spider. He uses his powers to fight crime and protect New York City as the superhero Spider-Man, balancing his superhero life with his personal responsibilities.",
                  "alter_ego": "Peter Parker",
                 "base": "New York City",
                  "comic_series": "The Amazing Spider-Man, Ultimate Spider-Man, Spider-Man 2099",
                "wisdom": 80,
                "raw_power": 75,
                "combat_skills": 90,
                "durability": 85,
                "intelligence": 90,
                "agility": 95,


            },

          {
            "name": "Superman",
            "universe": "DC",
            "powers": "Superhuman strength, speed, flight, heat vision, freeze breath, invulnerability",
             "first_power": "Superhuman Strength",
            "story": "Sent to Earth from Krypton as a baby, Kal-El grows up to become Superman, protector of Metropolis.",
            "real_creator": "Jerry Siegel, Joe Shuster",
             "movies": "Superman (1978), Superman II (1980), Superman III (1983), Superman IV: The Quest for Peace (1987), Superman Returns (2006), Man of Steel (2013), Batman v Superman: Dawn of Justice (2016), Justice League (2017)",
             "shows": "Smallville, Superman: The Animated Series",
              "main_image_url": "https://static.wikia.nocookie.net/dccomics/images/8/85/Superman_Rebirth_1.jpg",
            "bio": "Superman, born Kal-El on the planet Krypton, was sent to Earth as a baby to escape his planet's destruction. Raised as Clark Kent, he develops extraordinary powers and becomes a symbol of hope and justice, protecting Metropolis and the world from harm.",
                "alter_ego": "Clark Kent",
              "base": "Metropolis",
               "comic_series": "Action Comics, Superman, Superman: The Man of Steel",
            "wisdom": 95,
            "raw_power": 100,
            "combat_skills": 90,
            "durability": 100,
             "intelligence": 90,
            "agility": 90,


        },

{
                 "name": "Batman",
                "universe": "DC",
                 "powers": "Master detective, martial arts expert, uses high-tech gadgets",
                 "first_power": "Detective Skills",
                  "story": "After witnessing his parents' murder, Bruce Wayne dedicates his life to fighting crime as Batman.",
                  "real_creator": "Bob Kane, Bill Finger",
                   "movies": "Batman (1989), Batman Returns (1992), Batman Forever (1995), Batman & Robin (1997), Batman Begins (2005), The Dark Knight (2008), The Dark Knight Rises (2012), Batman v Superman: Dawn of Justice (2016), Justice League (2017), The Batman (2022)",
                   "shows": "Batman: The Animated Series, The Batman",
                  "main_image_url": "https://static.wikia.nocookie.net/marvel_dc/images/0/07/Batman_Vol_2_1.jpg",
                   "bio": "Bruce Wayne, a wealthy industrialist, witnessed the murder of his parents as a child. Driven by vengeance, he trained himself physically and intellectually to become Batman, a vigilante who protects Gotham City from criminals. Using his detective skills, technology, and martial arts prowess, he instills fear in the hearts of criminals and strives for justice.",
                 "alter_ego": "Bruce Wayne",
                 "base": "Gotham City",
                 "comic_series": "Detective Comics, Batman, The Dark Knight Returns",
                 "wisdom": 95,
                  "raw_power": 80,
                "combat_skills": 100,
                "durability": 85,
                  "intelligence": 100,
                   "agility": 90


             },
{
"name": "Wonder Woman",
"universe": "DC",
"powers": "Superhuman strength, speed, flight, agility, combat skills, magical weaponry",
 "first_power": "Superhuman Strength",
"story": "Amazonian princess Diana leaves her island paradise to fight for justice in the world of men.",
"real_creator": "William Moulton Marston",
"movies": "Wonder Woman (2017), Wonder Woman 1984 (2020)",
 "shows": "Wonder Woman (1975 TV series), Justice League",
"main_image_url": "https://static.wikia.nocookie.net/marvel_dc/images/c/cf/Wonder_Woman_Vol_5_1.jpg",
"bio": "Diana Prince, also known as Wonder Woman, is an Amazonian princess from the hidden island of Themyscira. Gifted with superhuman abilities and trained as a warrior, she leaves her home to fight for justice and peace in the world of man.  She wields powerful weapons like the Lasso of Truth and indestructible bracelets, and is a symbol of strength, compassion, and equality.",
  "alter_ego": "Diana Prince",
"base": "Themyscira, Washington D.C.",
"comic_series": "Wonder Woman, Sensation Comics, Wonder Woman (Rebirth)",
 "wisdom": 90,
 "raw_power": 95,
"combat_skills": 100,
"durability": 95,
"intelligence": 85,
"agility": 95


},
{
                 "name": "Thor",
                 "universe": "Marvel",
                  "powers": "Superhuman strength, speed, durability, flight, control of weather and lightning with Mjolnir",
                  "first_power": "Superhuman Strength",
                  "story": "Norse god of thunder who becomes a superhero on Earth.",
                    "real_creator": "Stan Lee, Larry Lieber, Jack Kirby",
                 "movies": "Thor (2011), Thor: The Dark World (2013), Thor: Ragnarok (2017), Avengers: Infinity War (2018), Avengers: Endgame (2019), Thor: Love and Thunder (2022)",
                 "shows": "The Avengers: Earth's Mightiest Heroes",
                  "main_image_url": "https://static.wikia.nocookie.net/marvel_dc/images/3/3c/ThorOdinson_Thor_Vol_6_1_Ross_Variant.jpg",
                    "bio": "Thor Odinson is the Asgardian God of Thunder, and a founding member of the Avengers. Wielding the enchanted hammer Mjolnir, he possesses immense strength, durability, and the ability to control lightning and weather. He is a powerful warrior and protector of both Asgard and Earth.",
                "alter_ego": "Donald Blake",
                  "base": "Asgard",
                "comic_series": "Journey into Mystery, Thor, The Mighty Thor",
                "wisdom": 85,
               "raw_power": 100,
                 "combat_skills": 95,
                "durability": 100,
                 "intelligence": 80,
                "agility": 85


            },
{
                 "name": "Hulk",
                "universe": "Marvel",
                 "powers": "Superhuman strength, durability, regeneration",
                "first_power": "Superhuman Strength",
                 "story": "Scientist Bruce Banner transforms into the Hulk when angered.",
                 "real_creator": "Stan Lee, Jack Kirby",
                  "movies": "Hulk (2003), The Incredible Hulk (2008), The Avengers (2012), Avengers: Age of Ultron (2015), Thor: Ragnarok (2017), Avengers: Infinity War (2018), Avengers: Endgame (2019)",
                "shows": "The Incredible Hulk (1996 TV series), Hulk and the Agents of S.M.A.S.H.",
                  "main_image_url": "https://static.wikia.nocookie.net/marveldatabase/images/7/71/Immortal_Hulk_Vol_1_1_textless.jpg",
                 "bio": "Dr. Bruce Banner, a brilliant physicist, was exposed to gamma radiation during a bomb test, transforming him into the Hulk, a creature of immense strength and rage. When angered, Banner transforms into the Hulk, a being of pure rage and incredible physical power.  He struggles to control his transformations and often finds himself at odds with both humanity and the forces that seek to exploit his power.",
                   "alter_ego": "Bruce Banner",
                "base": "Mobile",
                    "comic_series": "The Incredible Hulk, Tales to Astonish, Hulk",
                 "wisdom": 60,
                "raw_power": 100,
                "combat_skills": 80,
                 "durability": 100,
                 "intelligence": 100, #Bruce Banner is a genius
                 "agility": 70


            },
            {
                "name": "Captain America",
                 "universe": "Marvel",
                 "powers": "Peak human abilities, enhanced by Super-Soldier Serum, master tactician and martial artist",
                 "first_power": "Enhanced Strength and Speed",
                "story": "Frail Steve Rogers becomes a super-soldier during World War II.",
                 "real_creator": "Joe Simon, Jack Kirby",
                  "movies": "Captain America: The First Avenger (2011), The Avengers (2012), Captain America: The Winter Soldier (2014), Avengers: Age of Ultron (2015), Captain America: Civil War (2016), Avengers: Infinity War (2018), Avengers: Endgame (2019)",
                 "shows": "The Avengers: Earth's Mightiest Heroes",
                "main_image_url": "https://static.wikia.nocookie.net/marveldatabase/images/0/08/Captain_America_Vol_9_1_Coello_Variant.jpg",
                   "bio": "Steve Rogers, a frail young man from Brooklyn, was transformed into the super-soldier Captain America during World War II.  Enhanced with the Super-Soldier Serum, he possesses peak human abilities, exceptional combat skills, and unwavering moral principles. He is a leader and symbol of hope, fighting for freedom and justice.",
                    "alter_ego": "Steve Rogers",
                  "base": "The Avengers Mansion, New York City",
               "comic_series": "Captain America Comics, Tales of Suspense, Captain America",
                "wisdom": 95,
                "raw_power": 85,
                 "combat_skills": 100,
                "durability": 90,
                 "intelligence": 90,
                "agility": 90,


            },
             {
                "name": "Wolverine",
                "universe": "Marvel",
                  "powers": "Regeneration, superhuman senses, retractable adamantium claws",
                 "first_power": "Healing Factor",
                  "story": "Mutant with a mysterious past and powerful healing abilities.",
                 "real_creator": "Len Wein, John Romita Sr., Herb Trimpe",
                 "movies": "X-Men (2000), X2 (2003), X-Men: The Last Stand (2006), X-Men Origins: Wolverine (2009), The Wolverine (2013), X-Men: Days of Future Past (2014), X-Men: Apocalypse (2016), Logan (2017)",
                 "shows": "X-Men: The Animated Series, Wolverine and the X-Men",
                  "main_image_url": "https://static.wikia.nocookie.net/marvel_dc/images/9/94/Wolverine_Vol_7_1.jpg",
                  "bio": "Wolverine, also known as Logan, is a mutant with a powerful healing factor, enhanced senses, and retractable adamantium claws.  His past is shrouded in mystery, but he is a fierce warrior and a long-time member of the X-Men, fighting for mutant rights and protecting those he cares about.",
                  "alter_ego": "Logan",
                "base": "Xavier's School for Gifted Youngsters, The X-Mansion",
                 "comic_series": "The Incredible Hulk, Giant-Size X-Men, Wolverine",
                  "wisdom": 80,
                "raw_power": 85,
                "combat_skills": 100,
                  "durability": 95,  #Adamantium Skeleton
                 "intelligence": 80,
                "agility": 90


             },

{
                    "name": "Deadpool",
                 "universe": "Marvel",
                    "powers": "Regeneration, superhuman agility, master swordsman, breaks the fourth wall",
                    "first_power": "Regeneration",
                    "story": "Mercenary with a healing factor and a twisted sense of humor.",
                 "real_creator": "Fabian Nicieza, Rob Liefeld",
                 "movies": "X-Men Origins: Wolverine (2009), Deadpool (2016), Deadpool 2 (2018)",
                    "shows": "Ultimate Spider-Man",
                  "main_image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/4/49/Deadpool_cover.jpg/220px-Deadpool_cover.jpg",
                "bio": "Wade Wilson, subjected to experiments to cure his cancer, gained a powerful healing factor but was left disfigured and mentally unstable. He became the mercenary Deadpool, known for his exceptional combat skills, dark humor, and ability to break the fourth wall.",
                "alter_ego": "Wade Wilson",
                 "base": "Mobile",
                "comic_series": "The New Mutants, X-Force, Deadpool",
                 "wisdom": 60,
                 "raw_power": 80,
                 "combat_skills": 95,
                "durability": 95,
                    "intelligence": 80,
                  "agility": 95



                },
                  {
                    "name": "Iron Fist",
                        "universe": "Marvel",
                    "powers": "Master martial artist, can channel chi into his fist for superhuman strikes",
                 "first_power": "Iron Fist Punch",
                 "story": "Martial arts master who gains the power of the Iron Fist.",
                    "real_creator": "Roy Thomas, Gil Kane",
                   "movies": "N/A",  # No standalone movies yet
                       "shows": "Iron Fist (Netflix series)",
                       "main_image_url": "https://static.wikia.nocookie.net/marveldatabase/images/0/02/Iron_Fist_Vol_6_1.jpg",
                       "bio": "Danny Rand, trained in the mystical city of K'un-Lun, becomes the Iron Fist, a living weapon with the ability to channel his chi into a superhumanly powerful punch. He fights against injustice and protects the innocent.",
                "alter_ego": "Danny Rand",
                       "base": "K'un-Lun, New York City",
                    "comic_series": "Marvel Premiere, Iron Fist, The Immortal Iron Fist",
                   "wisdom": 90,
                      "raw_power": 85,
                     "combat_skills": 100,
                     "durability": 90,
                      "intelligence": 85,
                    "agility": 95

                },

                  {
                      "name": "Doctor Strange",
                      "universe": "Marvel",
                       "powers": "Master of magic, can manipulate time and space",
                    "first_power": "Astral Projection",
                    "story": "Skilled surgeon who becomes the Sorcerer Supreme.",
                     "real_creator": "Stan Lee, Steve Ditko",
                      "movies": "Doctor Strange (2016), Doctor Strange in the Multiverse of Madness (2022)",
                    "shows": "Ultimate Spider-Man, What If...?",
                      "main_image_url": "https://static.wikia.nocookie.net/marveldatabase/images/4/47/Doctor_Strange_Vol_5_1.jpg",
                      "bio": "Dr. Stephen Strange, a brilliant but arrogant surgeon, loses the use of his hands in an accident. He seeks a cure in the mystical arts and becomes the Sorcerer Supreme, protector of Earth against magical threats.",
                "alter_ego": "Stephen Strange",
                    "base": "Sanctum Sanctorum, New York City",
                     "comic_series": "Strange Tales, Doctor Strange, Sorcerer Supreme",
                    "wisdom": 100,
                        "raw_power": 95,
                       "combat_skills": 80,
                        "durability": 80,
                       "intelligence": 100,
                       "agility": 80


                  },
                 {
                    "name": "Black Panther",
                 "universe": "Marvel",
                    "powers": "Enhanced strength, speed, agility, senses; Vibranium suit",
                     "first_power": "Enhanced Senses",
                      "story": "King and protector of Wakanda, a technologically advanced nation.",
                     "real_creator": "Stan Lee, Jack Kirby",
                  "movies": "Captain America: Civil War (2016), Black Panther (2018), Avengers: Infinity War (2018), Avengers: Endgame (2019), Black Panther: Wakanda Forever (2022)",
                     "shows": "The Avengers: Earth's Mightiest Heroes",
                  "main_image_url": "https://static.wikia.nocookie.net/marveldatabase/images/f/ff/Black_Panther_Vol_7_1_textless.jpg",
                    "bio": "T'Challa is the Black Panther, king and protector of the technologically advanced African nation of Wakanda. Enhanced by the heart-shaped herb, he possesses superhuman abilities and wears a Vibranium suit, making him a formidable warrior and leader.",
                "alter_ego": "T'Challa",
                  "base": "Wakanda",
                    "comic_series": "Fantastic Four, Jungle Action, Black Panther",
                    "wisdom": 90,
                    "raw_power": 85,
                    "combat_skills": 100,
                    "durability": 95,
                     "intelligence": 95,
                   "agility": 95


                },

{
                   "name": "Aquaman",
                    "universe": "DC",
                    "powers": "Superhuman strength, speed, underwater breathing, telepathy with marine life",
                     "first_power": "Underwater Breathing",
                    "story": "King of Atlantis and protector of the seas.",
                 "real_creator": "Mort Weisinger, Paul Norris",
                   "movies": "Batman v Superman: Dawn of Justice (2016), Justice League (2017), Aquaman (2018)",
                    "shows": "Justice League,  Aquaman: King of Atlantis",
                    "main_image_url": "https://static.wikia.nocookie.net/marvel_dc/images/3/39/Aquaman_Vol_8_1.jpg",
                   "bio": "Arthur Curry, the Aquaman, is the King of Atlantis and ruler of the seven seas. He possesses superhuman strength, speed, the ability to breathe underwater, and can communicate with marine life. He is a fierce warrior and protector of the oceans.",
                  "alter_ego": "Arthur Curry",
                   "base": "Atlantis",
                   "comic_series": "More Fun Comics, Adventure Comics, Aquaman",
                    "wisdom": 85,
                      "raw_power": 90,
                      "combat_skills": 90,
                      "durability": 95,
                     "intelligence": 80,
                   "agility": 85


               },
# ... (Add more superheroes here - up to 30 total including the first two)
 {
                     "name": "Green Lantern (Hal Jordan)",
                     "universe": "DC",
                       "powers": "Wields a power ring that grants various abilities based on willpower",
                        "first_power": "Energy Construct Creation",
                       "story": "Test pilot chosen by a dying alien to wield a powerful ring.",
                     "real_creator": "John Broome, Gil Kane",
                     "movies": "Green Lantern (2011)",
                      "shows": "Justice League, Green Lantern: The Animated Series",
                      "main_image_url": "https://static.wikia.nocookie.net/marvel_dc/images/3/37/Green_Lantern_Vol_6_1.jpg",
                        "bio": "Hal Jordan, a fearless test pilot, was chosen by a dying alien to become a Green Lantern, a member of an intergalactic peacekeeping force. He wields a power ring that grants him a wide array of abilities fueled by his willpower, allowing him to create energy constructs, fly, and protect his sector of the universe.",
                  "alter_ego": "Hal Jordan",
                       "base": "Oa",
                     "comic_series": "Showcase #22, Green Lantern, Green Lantern Corps",
                     "wisdom": 80,
                      "raw_power": 95,
                       "combat_skills": 90,
                       "durability": 90,
                        "intelligence": 85,
                      "agility": 90



                 },
 {
                      "name": "The Flash (Barry Allen)",
                      "universe": "DC",
                     "powers": "Superhuman speed, can travel through time",
                 "first_power": "Superhuman Speed",
                      "story": "Forensic scientist gains superspeed after a lab accident.",
                    "real_creator": "Robert Kanigher, Carmine Infantino",
                      "movies": "Justice League (2017),  The Flash (2023)",
                   "shows": "The Flash (CW series)",
                   "main_image_url": "https://static.wikia.nocookie.net/marvel_dc/images/b/bd/Flash_Vol_5_1.jpg",
                       "bio": "Barry Allen, a forensic scientist, was struck by lightning and doused with chemicals, gaining superhuman speed and becoming the Flash. He uses his powers to fight crime and protect Central City, often traveling through time to prevent disasters.",
                     "alter_ego": "Barry Allen",
                       "base": "Central City",
                    "comic_series": "Showcase #4, The Flash, Flashpoint",
                 "wisdom": 85,
                       "raw_power": 90,
                     "combat_skills": 85,
                       "durability": 80,
                       "intelligence": 90,
                     "agility": 100





                 },

{
                 "name": "Cyborg",
                    "universe": "DC",
                    "powers": "Cybernetic enhancements grant superhuman strength, speed, and technology interface",
                   "first_power": "Enhanced Strength",
                  "story": "Half-human, half-machine hero who struggles with his identity.",
                    "real_creator": "Marv Wolfman, George Pérez",
                  "movies": "Justice League (2017), Zack Snyder's Justice League (2021)",
                      "shows": "Teen Titans,  Doom Patrol",
                  "main_image_url": "https://static.wikia.nocookie.net/dccomics/images/3/3f/Cyborg_Vol_2_1.jpg",
                  "bio": "Victor Stone, gravely injured in an accident, was saved by his scientist father who rebuilt him with cybernetic enhancements. Becoming Cyborg, he possesses superhuman strength, speed, and the ability to interface with technology, but struggles with his humanity and machine identity.",
                      "alter_ego": "Victor Stone",
                   "base": "Detroit",
                      "comic_series": "DC Comics Presents #26, The New Teen Titans, Cyborg",
                  "wisdom": 80,
                 "raw_power": 90,
                 "combat_skills": 85,
                 "durability": 95,
                  "intelligence": 95,
                    "agility": 85


             },
{
"name": "Hawkeye (Clint Barton)",
"universe": "Marvel",
 "powers": "Master archer and marksman, peak human conditioning",
"first_power": "Expert Archery",
 "story": "Skilled archer and agent of S.H.I.E.L.D.",
 "real_creator": "Stan Lee, Don Heck",
  "movies": "Thor (2011), The Avengers (2012), Avengers: Age of Ultron (2015), Captain America: Civil War (2016), Avengers: Endgame (2019)",
 "shows": "Avengers: Earth's Mightiest Heroes",
 "main_image_url": "https://static.wikia.nocookie.net/marveldatabase/images/4/43/Hawkeye_Vol_5_1_textless.jpg",
 "bio": "Clint Barton, also known as Hawkeye, is a master archer and marksman with peak human conditioning. He is a skilled agent of S.H.I.E.L.D. and a founding member of the Avengers, known for his exceptional accuracy and tactical expertise.",
 "alter_ego": "Clint Barton",
"base": "Avengers Compound",
 "comic_series": "Tales of Suspense, Hawkeye, Avengers",
 "wisdom": 85,
"raw_power": 70,
"combat_skills": 95,
"durability": 75,
"intelligence": 80,
 "agility": 90

 },


{
                    "name": "Black Widow (Natasha Romanoff)",
                      "universe": "Marvel",
                     "powers": "Master spy and assassin, peak human conditioning, expert martial artist",
                 "first_power": "Martial Arts",
                      "story": "Former KGB agent turned S.H.I.E.L.D. agent and Avenger.",
                     "real_creator": "Stan Lee, Don Rico, Don Heck",
                      "movies": "Iron Man 2 (2010), The Avengers (2012), Captain America: The Winter Soldier (2014), Avengers: Age of Ultron (2015), Captain America: Civil War (2016), Avengers: Infinity War (2018), Avengers: Endgame (2019), Black Widow (2021)",
                      "shows": "Avengers Assemble",
                        "main_image_url": "https://static.wikia.nocookie.net/marveldatabase/images/0/08/Black_Widow_Vol_8_1_textless.jpg",
                   "bio": "Natasha Romanoff, also known as Black Widow, is a highly trained spy, assassin, and martial artist.  A former KGB agent who defected to S.H.I.E.L.D., she became a key member of the Avengers, using her skills to fight for justice.",
                          "alter_ego": "Natasha Romanoff",
                 "base": "Avengers Compound",
                     "comic_series": "Tales of Suspense, The Avengers, Black Widow",
                        "wisdom": 90,
                        "raw_power": 75,
                     "combat_skills": 100,
                       "durability": 80,
                        "intelligence": 90,
                      "agility": 95



                 },
                    ]
        for hero_data in superhero_data:
            name = hero_data['name']
            universe = hero_data['universe']
            powers = hero_data['powers']
            # alice = hero_data['alice']
            main_image_url = hero_data['main_image_url']

            self.stdout.write(f"Processing {name}...")
            try:
                response = requests.get(main_image_url, stream=True, timeout=10)
                response.raise_for_status()
                if response.status_code == 200:
                    file_name = os.path.basename(main_image_url).split("?")[0]
                    image_data = BytesIO(response.content)
                    superhero = Superhero(name=name, universe=universe, powers=powers, listed_by=admin_user)
                    superhero.main_image.save(file_name, File(image_data))
                    self.stdout.write(self.style.SUCCESS(f'Successfully added {name} with image'))
                else:
                    self.stdout.write(self.style.ERROR(f"Error downloading image for {name}"))

            except requests.exceptions.RequestException as e:
                    self.stdout.write(self.style.ERROR(f"Error downloading image for {name}: {e}"))
            self.stdout.write(f"Finished processing: {name}")


        self.stdout.write(self.style.SUCCESS('Successfully populated superheroes!'))