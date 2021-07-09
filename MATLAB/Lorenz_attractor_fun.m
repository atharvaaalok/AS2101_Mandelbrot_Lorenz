function dYdt = Lorenz_attractor_fun(t, Y)
    % set values for constant appearing in the equation
    sigma = 10;
    rho = 28;
    beta = 8/3;
    % get variables
    x = Y(1);
    y = Y(2);
    z = Y(3);
    
    % calculate derivatives corresponding to each variable
    dxdt = sigma*(y-x);
    dydt = x*(rho-z) - y;
    dzdt = x*y - beta*z;
    
    % set vector of derivatives
    dYdt = [dxdt;dydt;dzdt];

end