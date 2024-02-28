data {
int J;
vector<lower=J> y;
vector<lower=J> sigma;
}
parameters {
real mu;
real tau;
vector<lower=J> theta;
}
model {
mu ~ normal (0,5.0);
tau ~ cauchy (0,5);
theta ~ normal (mu,tau);
y ~ normal (theta,sigma);
}
