% define time range over which to solve differential equation
tRange = [0 100];
% choose a deviation between the initial conditions
deviation = .01;
% first Initial Condition
x0_1 = 1;
y0_1 = 1;
z0_1 = 1;
Y0_1 = [x0_1; y0_1; z0_1];

% second initial condition
x0_2 = x0_1 + deviation;
y0_2 = y0_1 + deviation;
z0_2 = z0_1 + deviation;
Y0_2 = [x0_2; y0_2; z0_2];

% use ode45 to solve the system
[tSol_1, YSol_1] = ode45(@Lorenz_attractor_fun, tRange, Y0_1);
[tSol_2, YSol_2] = ode45(@Lorenz_attractor_fun, tRange, Y0_2);

xSol_1 = YSol_1(:,1);
ySol_1 = YSol_1(:,2);
zSol_1 = YSol_1(:,3);

xSol_2 = YSol_2(:,1);
ySol_2 = YSol_2(:,2);
zSol_2 = YSol_2(:,3);

% plot initial conditions
plot3(xSol_1(1), ySol_1(1), zSol_1(1), 'o', 'Color', 'white', 'MarkerFaceColor','white');
hold on
plot3(xSol_2(1), ySol_2(1), zSol_2(1), 'o', 'Color', 'white', 'MarkerFaceColor','white');

% plot trajectories
plot3(xSol_1, ySol_1, zSol_1, 'Color', 'red');
plot3(xSol_2, ySol_2, zSol_2, 'Color', 'blue');
hold off


grid on
% set background color to black - using hex color codes
set(gca, 'color', '#17202A');

saveas(gcf, 'Lorenz_attractor.png');
% set axis aspect ratio to 1:1:1
pbaspect([1 1 1]);