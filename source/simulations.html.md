---
title: Simulations
---

I am trying to present on this page various simulations I did over the past
years, and especially to give a few details about the SLE pictures I produced.
Some of the images produced are on [this page]({{site.baseurl}}/pictures.html).
Help yourself, use them as you see fit, just let me know. If you are interested
in the code, you can download the full source  for the last versions with
complete history and my current experiments if you have
[git](http://git.or.cz/). Just say

``` bash
git clone git://github.com/vbeffara/Simulations.git
```

Try them out, modify them, everything is under the GPL license. I develop
essentially on Mac OS X, but once in a while I check that everything compiles on
Linux. I tend to like experimenting with new features (typically the functional
stuff in C++11/C++14, and more recently OpenMP) so you mostly need a recent
compiler if you want to try things out.

Included in the source code is a separate library called `libvb` which is used
for both easily displaying pictures on screen during the simulation, and
producing a picture file in the end. It is not very well documented at this
point, but it should still be reasonably easy to use, reasonably cross-platform,
and it can save you a lot of time if you want to produce pictures yourself.


SLE - Schramm-Loewner Evolution
-------------------------------

The SLE pictures are obtained quite brutally by solving Loewner's
equation (using an Euler scheme) starting from various points in the
upper-half plane; the two shades of grey correspond to the sign of the
real part of $g(z)$ at time $1$ and the black curve is the boundary
between them, that is, the SLE trace. That is very easy to program, and
it gives very pleasing pictures at a controlled resolution; plus it
lends itself to various generic optimizations, especially knowing that
the boundary thus obtained is connected: Not all points have to be
computed.

The "tail" in the SLE pictures is due to a trick in the simulation; what
is represented is really obtained by using Loewner's equation driven by
a Brownian motion stopped at time $1$, and the SLE cluster at time $1$
is whatever appears on the picture, minus the smooth tail. (The trick is
that looking at the picture at time infinity, the complement of the
cluster has a right side and a left side, which is neat (see below); if
you know of any way to locate the point where the tail meets the
cluster, I am very interested in knowing how to do that ...)

There are of course other, more "complex analytical" ways to draw
pictures of SLE, the first one to come to mind being to use the reverse
flow and look at the images of the origin for various values of the time
parameter. The basic version of that is even easier to program, and the
main advantage is that one gets a list of points that are distributed
along the trace of the process, which can be plotted using any software.
[Tom Kennedy](http://math.arizona.edu/~tgk/) has a nice way of
optimizing the procedure. It is my (debatable) opinion that the pictures
obtained that way look somewhat nicer for small values of $\kappa$ but
are not as satisfying when $\kappa$ is greater than $4$, in particular
at the multiple points ...

One other way to proceed is to use the so-called [zipper
algorithm](http://www.math.washington.edu/~marshall/zipper.html)
introduced by Don Marshall, though I couldn't find any SLE pictures
produced this way online ...

Walks
-----

There are two very different kinds of walks present on the page. The
easiest one to describe, though apparently the most difficult to study,
is the (uniform) **self-avoiding walk**, which is just the uniform
measure on the set of discrete, self-avoiding paths of a given length.
The only efficient way to simulate that is known as the [pivot
algorithm](http://math.arizona.edu/~tgk/saw_pictures/index.html), which
is a Monte-Carlo method. Besides the spectral gap in this case is not
known, so it is not clear how precise the process is ...

The other kind present here is the **loop-erased walk**, which is just a
simple random walk from which all the loops are removed as soon as they
appear. This does *not* lead to a uniform distribution on the set of
paths; in fact, it is expected to have scaling exponent 5/4 whereas the
SAW should have exponent 4/3.

A third walk-related object is **DLA**, obtained as follows: Start on
the lattice $\mathbb{Z}^2$, with a core at the origin. Launch a simple
random walk "from infinity" (or equivalently, with a known distribution
on some large square), until it touches the core, and stop it there, so
that it sticks to the core. Then launch a second walk, which will stick
either to the core or to the final position of the first walk, and so
on. This generates a tree-like structure, about which not much is known
at all, but it provides with nice pictures anyway.

Lattice models
--------------

The easiest one to set up is **percolation**: on the lattice
$\mathbb{Z}^2$, declare each edge open with some probability $p$, and
closed with probability $1-p$, independently of all the others; then,
look for connected clusters of open edges. For all but a critical value
of the parameter, this model has a finite correlation length and thus
has no (non-trivial) scaling limit; but at criticality (in this case,
when $p=1/2$), one expects a non-trivial limit to exist. Represented are
two samples of large clusters at criticality.

The **gradient percolation** model is the same thing except that the
parameter $p$ depends on the location of the edge. In other words, it
will be subcritical at some places and supercritical at others, and
interesting things happen around the boundary between these two regions.

The **Ising model** describes the interaction of ferromagnetic spins on
a lattice. The picture on the page is a sample of this model taken at
criticality, on a $1000 \times 1000$ grid, with boundary conditions that
are white on the left and black on the right, generated by [perfect
simulation](http://dbwilson.com/exact/), using the "coupling from the
past" technique. The interface is supposed to look like an SLE for
$\kappa=3$ ... You can try to generate larger samples, but CFTP takes
forever: this one took about 4 hours.
