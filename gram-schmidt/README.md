**Definition**: Let V be a normed vector space with an inner product. An orthogonal projection of v onto w is given by:

Proj_w(v) = (⟨v, w⟩ / ⟨w, w⟩) w

# Classical Orthonormalization Process

Let B = {v_1, v_2, ..., v_n} be a basis for a vector space V. We will represent the orthogonal basis as Q and the orthonormal basis as Q*.

1. **Orthogonalization of the Basis**:  
   For each v_i in B, obtain its corresponding q_i:
   
   q_n = v_n - Proj_{q_{n-1}}(v_n) - Proj_{q_{n-2}}(v_n) - ... - Proj_{q_1}(v_n)

2. **Orthonormalization of the Basis**:  
   For each q_i in Q, obtain its corresponding q_i*:
   
   q_i* = q_i / ||q_i||

# Modified Orthonormalization Process

**Definition**: Let V be a normed vector space with an inner product. An orthogonal projection of v onto w is given by:

Proj_w(v) = (⟨v, w⟩ / ⟨w, w⟩) w

Let B = {v_1, v_2, ..., v_n} be a basis for a vector space V. We will represent the orthogonal basis as Q and the orthonormal basis as Q*.

1. **Orthogonalization of the Basis**:  
   For each v_i in B, obtain its corresponding q_i using the following steps:
   - Initialize q_1 = v_1
   - For i = 2 to n:
     
     q_i = v_i - Σ_{j=1}^{i-1} Proj_{q_j}(v_i)

2. **Orthonormalization of the Basis**:  
   For each q_i in Q, obtain its corresponding q_i*:
   
   q_i* = q_i / ||q_i||
