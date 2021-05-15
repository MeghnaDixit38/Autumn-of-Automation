# Paper Summary

{% embed url="https://drive.google.com/file/d/1S2DlJ7z5GgC9V8KUiXxuaev9C-hzUPBV/view?usp=sharing" %}

Summary:

Quadrotors are typically controlled by neglecting aerodynamic effects, such as rotor drag, that only become important for non-hover conditions. These aerodynamic effects are treated as unknown disturbances, which works well when controlling the quadrotor close to hover conditions but reduces its trajectory tracking accuracy progressively with increasing speed. The common model of a quadrotor without considering rotor drag effects is differentially flat when choosing its position and heading as flat outputs. Running a Nelder-Mead gradient free optimization for which the quadrotor repeats a predefined trajectory in each iteration of the optimization. During this procedure, we control the quadrotor by the proposed control scheme with different drag coefficients in each iteration during which we record the absolute trajectory tracking error and use it as cost for the optimization. Once the optimization has converged, we know the coefficients that reduce the trajectory tracking error the most. This procedure has the advantage that no IMU and rotor speed measurements are required, which are both unavailable on our quadrotor platform used for the presented experiments, and the gyro measurements do not need to be differentiated. The dynamical model of a quadrotor subject to linear rotor drag effects is differentially flat. This property was exploited to compute feed-forward control terms as algebraic functions of a reference trajectory to be tracked. We presented a control policy that uses these feed-forward terms, which compensates for rotor drag effects, and therefore improves the trajectory tracking performance of a quadrotor already from speeds of 0.5 m s−1 onwards. The proposed control method reduces the root mean squared tracking error by 50 % independently of the executed trajectory.

{% embed url="https://drive.google.com/file/d/1PQnMYiTYTlfAzdjUxDqImJOelr3Exry-/view?usp=sharing" %}



