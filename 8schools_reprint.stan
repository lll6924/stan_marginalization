data {
int<lower=0> J;
vector[J] y;
vector<lower=0>[J] sigma;
}
parameters {
real mu;
real<lower=0> tau;
vector[J] theta;
}
model {
mu ~ normal (0,5.0);
tau ~ cauchy (0,5);
theta ~ normal (mu,tau);
y ~ normal (theta,sigma);
}
