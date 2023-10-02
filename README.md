# Wisconsin-Autonomous-Perception-Coding-Challenge---Aran-Viswanath
![Uploading answer.png…]()

At first I tried to find the cones on the unmodified image but ran into 2 problems: It took way too long and the exit signs in the back were counted in the analysis. Because of this I reduced the size of the image and blurred it to get rid of the exit sign while maintaining the prominence of the cones. Then I took the x y coordinates and ran it through a regression to find a linear equation to represent the boundaries presented by the cones. Then I drew blue lines and adjusted their size to make them more visible.
