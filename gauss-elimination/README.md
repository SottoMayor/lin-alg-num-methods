# Gauss Elimination and Row Echelon Form

## General Idea

Gauss elimination is a method used to solve systems of linear equations. The goal is to transform the matrix associated with the system into an echelon form, facilitating the resolution of the equations through back substitution. The process involves two main steps:

1. Echelon Form: Using row elementary operations, the matrix is transformed into an echelon form, where all elements below each pivot (1) are zeros.

2. Back Substitution: Once the matrix is in echelon form, the equations can be solved starting from the last equation and substituting the values found into the previous equations.

## Algorithm

### Step-by-Step Gauss Elimination for a 2x2 System

**System Representation**:
   - L1: ` a_11x + a_12y = b_1 `
   - L2: `a_21x + a_22y = b_2 `

1. **Step 1**: `a_11` should be 1.
   - Take the value of `a_11` and multiply `L1` by `( 1/(a_11) )`.

2. **Step 2**: Elimination of `a_21`.
   - Select `a_21`.
   - Multiply `L2` by `(-1 / a_21)` and add it to `L1`.
   - Place the result of the sum in place of `L2`.

3. **Step 3**: Find `y` and substitute `y` back into `L1` to find `x`.


### Step-by-Step Gauss Elimination for a (n x m) System

1. **Step 1: Pivot Selection**:
   - For each column `j` of the matrix, select a non-zero element `a_ii` as the pivot in row `i`, such that `i >= j`.
   - If `a_ii` is not 1, divide the entire row `i` by `a_ii` to make the pivot equal to 1.

2. **Step 2: Eliminate Elements Below the Pivot**: 
   - To eliminate all elements below the pivot `a_ii`, for each row `k > i`, multiply row `k` by `(-1 / a_kj)`, so that a_kj becomes -1, and sum it with the pivot's row. So the new row `L_newK = L_i + L_k` substitutes the previous `L_k`.
   - This ensures that all elements below the pivot `a_ii` become zero.

4. **Step 3: Repeat for All Relevant Columns**:
   - Move to the next column `j+1` and repeat the steps above until you have processed all the columns corresponding to variables, considering the `a_ii` as pivot

5. **Step 4: Back Substitution**:
   - Once the matrix is in upper triangular form (the echelon form), solve the last equation and use back substitution to find the remaining variables.



