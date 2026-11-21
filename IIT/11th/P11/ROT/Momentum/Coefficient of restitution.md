#mechanics #collision #momentum #worked_example
## how bouncy a collision is
$$
e=\frac{\text{speed of separation}}{\text{speed of approach}}=\frac{v_2-v_1}{u_1-u_2}
$$
^restitution

measured **along the line of impact** (the line joining the centres, or ⊥ to a wall). part of [[Rotational mechanics]]

| $e$ | collision | KE |
|---|---|---|
| $1$ | elastic ([[Elastic collisions]]) | kept |
| $0<e<1$ | partly elastic | some lost |
| $0$ | perfectly inelastic, they stick ([[Perfectly inelastic collisions]]) | most lost |

> [!important] the one idea
> ==$e$ compares relative speeds, not the speeds themselves: use it with momentum conservation to get both final velocities==. a moving wall counts too: use the speed relative to the wall

> [!eg] two balls
> 10 m/s catches 4 m/s; after: 2 m/s and 5 m/s. $e=\frac{5-2}{10-4}=\frac36=0.5$

## a ball bouncing on the floor
dropped from $h_1$, it hits at $\sqrt{2gh_1}$, leaves at $e\sqrt{2gh_1}$ and rises to $h_2=e^2h_1$:
$$
e=\sqrt{\frac{h_2}{h_1}}
$$
^bounce-e

dropped from 8 m, bounces to 2 m: $e=\sqrt{\frac28}=0.5$

![[Bouncing_ball_restitution_animation.png]]

## moving walls
the wall is so heavy its velocity doesn't change, so only the ball's velocity is unknown. take right as $+$, $e=0.5$
- **wall coming towards the ball**: ball at $+4$ m/s, wall at $-2$ m/s. approach $4-(-2)=6$, so they separate at $3$: the ball leaves at $-2-3=-5$, **5 m/s** to the left (faster than it came)
- **wall moving away**: ball at $+10$ m/s, wall at $+2$ m/s. approach $8$, separate at $4$: the ball leaves at $2-4=-2$, **2 m/s** to the left

## an oblique hit on a wall
a ball hits a smooth wall at speed $u$, at angle $\theta_1$ to the normal, and leaves at $v$, $\theta_2$
- along the wall: no force (smooth), so $v\sin\theta_2=u\sin\theta_1$
- ⊥ to the wall: $e$ applies, so $v\cos\theta_2=e\,u\cos\theta_1$

$$
\tan\theta_2=\frac{\tan\theta_1}{e},\qquad v=u\sqrt{\sin^2\theta_1+e^2\cos^2\theta_1}
$$

the ball leaves at a **flatter** angle (further from the normal) when $e<1$

> [!exercise] try these
> **1** a ball dropped from 5 m bounces to 1.8 m. find $e$
> **2** same ball, how high is the second bounce?
> **3** a ball hits a wall at 10 m/s, $45°$ to the normal, $e=0.5$. speed and angle after?

> [!answer]-
> **1** $e=\sqrt{1.8/5}=0.6$
> **2** $0.6^2\times1.8=0.648$ m
> **3** along: $7.07$, normal: $3.54$; $v\approx7.9$ m/s, $\tan\theta_2=2$, $\theta_2\approx63°$

see also [[Impulse]], [[Free rod collisions]]

hub: [[Rotational mechanics]]
