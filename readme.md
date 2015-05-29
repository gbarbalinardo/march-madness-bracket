Introduction
======

This repo a Monte Carlo simulation of the NCAA tournament. Input stats are taken from [kenpom](http://kenpom.com/) and are referred to March 2015. More details can be found [here](http://blog.grio.com/2015/05/parallel-computing-with-a-gpu).


Technical Details
=====
### CUDA
The python script uses Cuda, parallel GPU, to improve performaces. It require NumbaPro to run properly. 

### NumbaPro
The methods in the code get parallelize using the Numbapro decorators. See the [official documentation](http://docs.continuum.io/numbapro/quickstart.html) for more information.

* **vectorize:** The vectorize decorator produces a NumPy Universal function (ufunc) object from a python function. A ufunc can be overloaded to take multiple combination parameter types. User must provide a list of function types as the first argument of vectorize.
* **guvectorize:** The guvectorize decorator produces a NumPy Generalized Univesral function (gufunc) object from a python function. While vectorize works on scalar arguments, guvectorize works on array arguments. This decorator takes an extra argument for specifying gufunc signature. Please refer to NumPy documentations for details of gufunc.

Feedback, comments
=====
For any comment, feedback and request please contact me at giuseppe.barbalinardo@gmail.com.
