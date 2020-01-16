import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story',
                        'A Story of a boy and his toys that come to life',
                        'https://throughtwoblueeyes.files.wordpress.com/2014/04/toy_story_1995_4.jpg',
                        'https://www.youtube.com/watch?v=rNk1Wi8SvNc',
                        'https://www.youtube.com/watch?v=yEqMuknF5C8')
taitanic = media.Movie('Taitanic',
                       'Story about destruction of largest ship Taitanic',
                       'http://allhdwallpapers.com/wp-content/uploads/2015/04/titanic-6.jpg',
                       'https://www.youtube.com/watch?v=kVrqfYjkTdQ',
                       'https://www.youtube.com/watch?v=YQB_Dzyo0DE')
                       
three_idiots = media.Movie('3 Idiots',
                           'A funny story about three college friends',
                           'https://i2.wp.com/www.meinstyn.com/wp-content/uploads/2017/01/3-Idiots-Movie-Poster-Aamir-Khan-Kareena-Kapoor-R-Madhavan-Sharman-Joshi-Full-HD-Desktop-Wallpaper.jpg?fit=1190%2C1600&ssl=1',
                           'https://www.youtube.com/watch?v=K0eDlFX9GMc',
                           'https://www.youtube.com/watch?v=y5VUKEtPsnc')
grand_masti = media.Movie('Grand Masti',
                          'A awesome comedy film',
                          'http://1.bp.blogspot.com/-3ZUbfgSyEBc/UhWqa4ri5wI/AAAAAAAATKg/dgDJ-e8r_E0/s640/Grand-Masti-Hindi-Movie-First-Look-Posters+(1).jpg',
                          'https://www.youtube.com/watch?v=8L4qT6-fNzQ',
                          'https://www.youtube.com/watch?v=H-KJYTYmXfM')
                          
ronal_the_barbarian = media.Movie('Ronal The Barbarian',
                                  'Fantasy comedy about young Ronal who lives in a barbarian village.',
                                  'https://media.baselineresearch.com/images/613914/613914_full.jpg',
                                  'https://www.youtube.com/watch?v=oJpTdNSzB0E',
                                  'https://www.youtube.com/watch?v=aX6WTAYSz-s')
ratatouille = media.Movie('Ratatouille',
                          'A rat is a chef in Paris',
                          'https://clubfleurieu.com/wp-content/uploads/2017/07/ratatouillec-movie-poster.jpg',
                          'https://www.youtube.com/watch?v=NgsQ8mVkN8w',
                          'https://www.youtube.com/watch?v=B5JOTWsXtT4')
midnight_in_paris = media.Movie('Midnight in Paris',
                                'Going back in time to meet author',
                                'https://myfrugaladventures.com/wp-content/uploads/2012/02/midnight-in-paris.jpg',
                                'https://www.youtube.com/watch?v=FAfR8omt-CY',
                                'https://www.youtube.com/watch?v=IRk1YYfofBc')
hunger_games = media.Movie('Hunger Games',
                           'A really real reality show',
                           'http://movieposters.ie/wp-content/uploads/2012/04/hunger-games-french.jpg',
                           'https://www.youtube.com/watch?v=PbA63a7H0bo',
                           'https://www.youtube.com/watch?v=KsnbcoK7xho')
movies = [toy_story, taitanic,three_idiots, grand_masti, ronal_the_barbarian, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
                           
                                
                              
                           
                        
