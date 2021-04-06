#!/usr/bin/env python

import numpy as np
import time


def sum_v0(n):
    return n*(n-1)/2

def sum_v1(n):
    vals = np.arange(n)
    return np.sum(vals)

def sum_v2(n):
    return sum(np.arange(n))

def sum_v3(n):
    vals = np.arange(n)
    running_sum = 0
    for i in range(len(vals)):
        running_sum += vals[i]
    return running_sum

def sum_v4(n):
    running_sum = 0
    for i in range(n):
        running_sum += i
    return running_sum

def cumul_sum_v0(n):
    vals = np.arange(n)
    return np.cumsum(vals)

def cumul_sum_v1(n):
    vals = np.arange(n)
    return vals*(vals+1)/2

def cumul_sum_v2(n):
    vals = np.arange(n)
    out_vals = np.zeros((n))
    running_sum = 0
    for i in range(len(vals)):
        running_sum += vals[i]
        out_vals[i] = running_sum
    return out_vals

def cumul_sum_v3(n):
    out_vals = np.zeros((n))
    running_sum = 0
    for i in range(n):
        running_sum += i
        out_vals[i] = running_sum
    return out_vals
        
def cumul_sum_v4(n):
    out_vals = np.zeros((n))
    for i in range(1,n):
        out_vals[i] = out_vals[i-1] + i
    return out_vals

def cumul_sum_v5(n):
    out_vals = [0]
    for i in range(1,n):
        out_vals.append(i + out_vals[-1])
    return np.array(out_vals)

def cumul_sum_v6(n):
    out_vals = []
    running_sum = 0
    for i in range(n):
        running_sum += i
        out_vals.append(running_sum)
    return np.array(out_vals)

def squares_v0(v):
    return v*v

def squares_v1(v):
    def sq(x):
        return x*x
    return np.array([sq(x) for x in v])

def squares_v2(v):
    sq = lambda x : x*x
    return np.array([sq(x) for x in v])

def squares_v3(v):
    def sq(x):
        return x*x
    sq_vect = np.vectorize(sq)
    return sq_vect(v)
    
def squares_v4(v):
    sq = lambda x : x*x    
    sq_vect = np.vectorize(sq)
    return sq_vect(v)

def matmul_v0(m1, m2):
    return np.matmul(m1, m2)

def matmul_v1(m1, m2):
    return np.sum(np.expand_dims(m1, -1).swapaxes(1,2) * np.expand_dims(m2, -1).swapaxes(0,2), axis=2)

def matmul_v2(m1, m2):
    nrow = m1.shape[0]
    ncol = m1.shape[1]
    out = np.zeros((nrow, ncol))
    for i in range(nrow):
        for j in range(ncol):
            out[i,j] = np.sum(m1[i]*m2.T[j])
    return out

def matmul_v3(m1, m2):
    nrow = m1.shape[0]
    ncol = m1.shape[1]
    return np.array([[sum([m1[i,k] * m2[k,j] for k in range(nrow)]) for j in range(ncol)] for i in range(nrow)])

def matmul_v4(m1, m2):
    nrow = m1.shape[0]
    ncol = m1.shape[1]
    out = []
    for i in range(nrow):
        outcol = []
        for j in range(ncol):
            outcol.append(np.sum(m1[i]*m2.T[j]))
        out.append(outcol)
    return np.array(out)

def matmul_v5(m1, m2):
    nrow = m1.shape[0]
    ncol = m1.shape[1]
    out = np.zeros((nrow, ncol))
    for i in range(nrow):
        for j in range(ncol):
            sum = 0.
            for k in range(nrow):
                sum += m1[i,k] * m2[k,j]
            out[i, j] = sum
    return np.array(out)

def matmul_v6(m1, m2):
    nrow = m1.shape[0]
    ncol = m1.shape[1]
    out = np.zeros((nrow, ncol))
    for i in range(nrow):
        for j in range(ncol):
            for k in range(nrow):
                out[i, j] += m1[i,k] * m2[k,j]
    return np.array(out)

def matmul_v7(m1, m2):
    nrow = m1.shape[0]
    ncol = m1.shape[1]
    out = []
    for i in range(nrow):
        outcol = []
        for j in range(ncol):
            sum = 0
            for k in range(nrow):
                sum = sum + m1[i,k] * m2[k,j]
            outcol.append(sum)
        out.append(outcol)
    return np.array(out)

def matmul_v8(m1, m2):
    nrow = m1.shape[0]
    ncol = m1.shape[1]
    out = np.zeros((nrow, ncol))
    for k in range(nrow):
        for j in range(ncol):
            for i in range(nrow):
                out[i, j] += m1[i,k] * m2[k,j]
    return np.array(out)

def matmul_v9(m1, m2):
    return np.sum(m1[:,None,:] * m2.T[None,:,:], axis=2)


def time_func(func, n, ref_time):
    t0 = time.time()
    val = func(n)
    t1 = time.time()
    dt = t1 - t0
    if ref_time is None:
        ref_time = dt
    print("%s(%i) = %i, dt=%.4e, factor=%.1f" % (str(func), n, val, dt, dt/ref_time))
    return dt

def time_cumul_func(func, n, ref_time):
    t0 = time.time()
    vals = func(n)
    t1 = time.time()
    dt = t1 - t0
    if ref_time is None:
        ref_time = dt
    print("%s(%i) = %i, dt=%.4e, factor=%.1f" % (str(func), n, vals[-1], dt, dt/ref_time))
    return dt

def time_sq_func(func, v, ref_time):
    t0 = time.time()
    vals = func(v)
    t1 = time.time()
    dt = t1 - t0
    if ref_time is None:
        ref_time = dt
    print("%s(%i) = %.2e, dt=%.4e, factor=%.1f" % (str(func), len(v), vals[-1], dt, dt/ref_time))
    return dt
    
def time_matmul_func(func, m1, m2, check, ref_time):
    t0 = time.time()
    vals = func(m1, m2)
    t1 = time.time()
    diff = vals - check
    dt = t1 - t0
    if ref_time is None:
        ref_time = dt
    print("%s%s +- %.2e, %.2e, dt=%.4e, factor=%.1f" % (str(func), m1.shape, np.min(diff), np.max(diff), dt, dt/ref_time))
    return dt
    
SUM_FUNCS = [sum_v0, sum_v1, sum_v2, sum_v3, sum_v4]
CUMULSUM_FUNCS = [cumul_sum_v0, cumul_sum_v1, cumul_sum_v2, cumul_sum_v3, cumul_sum_v4, cumul_sum_v5, cumul_sum_v6]
SQ_FUNCS = [squares_v0, squares_v1, squares_v2, squares_v3, squares_v4]
MATMUL_FUNCS = [matmul_v0, matmul_v1, matmul_v2, matmul_v3, matmul_v4, matmul_v5, matmul_v6, matmul_v7, matmul_v8, matmul_v9]

N = 1000000
VECT = np.linspace(0, 1, N)
MSIZE = 200

M1 = np.random.normal(np.zeros((MSIZE, MSIZE)))
M2 = np.random.normal(np.zeros((MSIZE, MSIZE)))
MCHECK = np.matmul(M1, M2)

def main():

    ref_sum = None
    for func in SUM_FUNCS:
        dt = time_func(func, N, ref_sum)
        if ref_sum is None:
            ref_sum = dt

    ref_cumsum = None
    for func in CUMULSUM_FUNCS:
        dt = time_cumul_func(func, N, ref_cumsum)
        if ref_cumsum is None:
            ref_cumsum = dt
        
    ref_squares = None
    for func in SQ_FUNCS:
        dt = time_sq_func(func, VECT, ref_squares)
        if ref_squares is None:
           ref_squares  = dt

    ref_mat_mul = None
    for func in MATMUL_FUNCS:
        dt = time_matmul_func(func, M1, M2, MCHECK, ref_mat_mul)
        if ref_mat_mul is None:
            ref_mat_mul = dt

main()

        



    


    
