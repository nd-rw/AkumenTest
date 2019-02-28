# Sample Akumen R Model

# Important sections of this are noted with !!'s.

akumen <- function(first, second, ...) {
    # !! This akumen() connector function must exist!
	
	# Parameters:
	# 	!! These lines define parameters, and a line must exist per input (or output).

    #    - Input: first [float]
    #    - Input: second [float]

    #    - Output: first_result [float]
    #    - Output: second_result [float]


    # Our model code goes here (including any calls to other functions, modules or libraries)
	first_result <- first + second
	second_result <- first - second

    # Images can be viewed through the Research Grid, if they are saved to outputs.
    png(filename="outputs/example.png")
    plot(c(first, second, first_result, second_result))
    dev.off()

    # The akumen() function must return a dictionary including keys relating to outputs.
	ret <- list()
	ret[["first_result"]] <- first_result
	ret[["second_result"]] <- second_result
	return(ret)
}

if (!exists("REMOTE")) {
	# Any local test code can be used in a block like this.
    # When developing on a local machine, you can put code 
    # here that won't get run by Akumen.
	print(akumen(1, 2))
}

