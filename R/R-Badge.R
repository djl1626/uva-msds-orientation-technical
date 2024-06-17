# Euler 1
sum <- 0
for(i in 1:999) {
  if (i %% 3 == 0 | i %% 5 == 0) {
    sum <- sum + i
  }
}
print(sum)

# Euler 2
prev <- 1
nxt <- 2
sum <- 2
while (prev < 4000000 & nxt < 4000000) {
  temp <- prev + nxt
  prev <- nxt
  nxt <- temp
  if (nxt %% 2 == 0 & nxt < 4000000) {
    sum <- sum + nxt
  }
}
print(sum)

# Euler 3
isPrime <- function(n) {
  if (n == 2) {
    return(TRUE)
  } else if (n %% 2 == 0) {
    return(FALSE)
  }
  factor <- 3
  while (factor <= as.integer(sqrt(n)) + 1) {
    if (n %% factor == 0) {
      return(FALSE)
    }
    factor <- factor + 2
  }
  return(TRUE)
}
max <- 3
j <- 3
num <- 600851475143
while (num > 1) {
  if (num %% j == 0 & isPrime(j)) {
    max <- j
  }
  while (num %% j == 0) {
    num <- num / j
  }
  j <- j + 1
}
print(max)

# Distributions
library(tidyverse)
binom <- as.data.frame(rbinom(1000, 100, .1))
names(binom) <- c("random_data")
ggplot(binom, aes(x=random_data)) + geom_histogram(bins=20)
uniform <- as.data.frame(runif(1000))
names(uniform) <- c("random_data")
uniform %>% ggplot(aes(x=random_data)) + geom_histogram()
chi <- as.data.frame(rchisq(1000, 3))
names(chi) <- c("random_data")
chi %>% ggplot(aes(x=random_data)) + geom_histogram()