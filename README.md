# SLChildren
Technology: python multilayer perceptron code for learning level detection,front end using flask and bootstrap,video search through YOUTUBEAPI.

Personalized learning material for students with special needs using machine learning.

Its a website that help austism children to learn from internet and test their learning using puzzle.

Children with neurological disorder such as autism need personalized development system for their daily activities. 
For them technology can play a significant role. Personalized learning models can give each student differentiated learning experiences based on their needs, interests, and strengths including students with disabilities. 
Our system delivers personalized learning materials for children with special needs based on diverse characteristics of children.There are four parts of the system:
i) identify level of the user by using machine learning algorithm. 
ii) Web mining to generate multimodal learning materials for text story or learning keywords, 
iii) linking user preferences with the result, 
iv) personalizing contents for users delineated with an intelligent interface. 


There are two user one is autism children and other is teacher/ guide of autism children. They must first signup with their account. 
Teacher give rating to their reading , writing , speaking , listening , disability, mobility in the range of 1 to 5 .(1 for lowest , 5 for highest). 
In background multilayer perceptron machine learning algorithm predicts the learning level of child and store it in the database.(level of learning could be LOW, NORMAL, GOOD, EXCELLENT).

Students can search for a keyword using the site. He can see images as well as videos according to his preference.The search results and number of results differ for different level of children.

Students can also under text story if they are not able to understand after reading.

Student enter text story for images / videos search from internet. From the entered story important keyword were extracted. Images are search on google using python libraries and videos are searches using youtube api. We collected all video ids and processed them to see videos on our web pages. Before feeding results to students , results were filtered based on authenticated sites like .edu, .in, .gov, etc.

we have provided stories on web pages from where students can learn story from videos. 

Autism children face difficulty in learning objects . so we have made a puzzle from where children can learn different images (remember images) and test their learning using puzzle. Images are shown first then according to learning level image get scattered into 2 or 3 or 4. User needs to place them in right place.
