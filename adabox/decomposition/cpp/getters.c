
#include "stdio.h"
#include "stdlib.h"

int square(int i) {
	return i * i;
}

int get_bottom_distance(int idx_i_arg, int idx_j_arg, int n_arg, int lim, int *data_matrix_arg){
    int di =0;
    int temp_val = 0;
    for (int i=idx_i_arg; i<lim; i++){
        temp_val = data_matrix_arg[i * n_arg + idx_j_arg];
        if(temp_val == 0){
            break;
        }
        di++;
    }
    return di;
}

int get_top_distance(int idx_i_arg, int idx_j_arg, int n_arg, int lim, int *data_matrix_arg){
    int di = 0;
    int temp_val = 0;
    for (int i=idx_i_arg; i>lim; i--){
        temp_val = data_matrix_arg[i * n_arg + idx_j_arg];
        if(temp_val == 0){
            break;
        }
        di++;
    }
    return di;
}

// results matrix: [x1 x2 y1 y2]
void get_right_bottom_rectangle(int idx_i_arg, int idx_j_arg, long m_arg, long n_arg, int *data_matrix_arg, int *results){

    int x1_val = 0;
    int x2_val = 0;
    int y1_val = 0;
    int y2_val = 0;

    int d0, dj;

    d0 = get_bottom_distance( idx_i_arg, idx_j_arg, n_arg,  m_arg, data_matrix_arg);

    dj = 0;
    for (int j=idx_j_arg + 1; j<n_arg; j++){
        int di = get_bottom_distance(idx_i_arg, j, n_arg, idx_i_arg + d0, data_matrix_arg);
        if (di < d0){
            break;
        }
        dj++;
    }

    x1_val = idx_j_arg;
    y1_val = idx_i_arg;
    x2_val =  idx_j_arg + dj;
    y2_val =  idx_i_arg + d0 - 1;

    results[0] = x1_val;
    results[1] = x2_val;
    results[2] = y1_val;
    results[3] = y2_val;

}



void get_left_bottom_rectangle(int idx_i_arg, int idx_j_arg, long m_arg, long n_arg, int *data_matrix_arg, int *results){


    int x1_val = 0;
    int x2_val = 0;
    int y1_val = 0;
    int y2_val = 0;


    int d0,dj;

    d0 = get_bottom_distance( idx_i_arg, idx_j_arg, n_arg, m_arg, data_matrix_arg);
    dj = 0;
    for (int j=idx_j_arg - 1; j>=0; j--){

        int di = get_bottom_distance( idx_i_arg, j, n_arg, idx_i_arg + d0, data_matrix_arg);

        if (di < d0){
            break;
        }
        dj++;
    }

    x1_val = idx_j_arg;
    y1_val = idx_i_arg;
    x2_val = idx_j_arg - dj;
    y2_val = idx_i_arg + d0 - 1;


    results[0] = x1_val;
    results[1] = x2_val;
    results[2] = y1_val;
    results[3] = y2_val;
}



void get_left_top_rectangle(int idx_i_arg, int idx_j_arg, long n_arg, int *data_matrix_arg, int *results){


    int x1_val = 0;
    int x2_val = 0;
    int y1_val = 0;
    int y2_val = 0;


    int d0, dj;

    d0 = get_top_distance( idx_i_arg, idx_j_arg, n_arg, -1, data_matrix_arg);
    dj = 0;
    for (int j=idx_j_arg - 1; j>-1; j--){

        int di = get_top_distance( idx_i_arg, j, n_arg, idx_i_arg - d0, data_matrix_arg);
        if (di < d0){
            break;
        }
        dj++;
    }

    x1_val = idx_j_arg;
    y1_val = idx_i_arg;
    x2_val = idx_j_arg - dj;
    y2_val = idx_i_arg - d0 + 1;


    results[0] = x1_val;
    results[1] = x2_val;
    results[2] = y1_val;
    results[3] = y2_val;
}


void get_right_top_rectangle(int idx_i_arg, int idx_j_arg, long n_arg, int *data_matrix_arg, int *results){


    int x1_val = 0;
    int x2_val = 0;
    int y1_val = 0;
    int y2_val = 0;


    int d0, dj;

    d0 = get_top_distance( idx_i_arg, idx_j_arg, n_arg, -1, data_matrix_arg);
    dj = 0;
    for (int j=idx_j_arg + 1; j<n_arg; j++){
        int di = get_top_distance( idx_i_arg, j, n_arg, idx_i_arg - d0, data_matrix_arg);
        if (di < d0){
            break;
        }
        dj++;
    }

    x1_val = idx_j_arg;
    y1_val = idx_i_arg;
    x2_val = idx_j_arg + dj;
    y2_val = idx_i_arg - d0 + 1;


    results[0] = x1_val;
    results[1] = x2_val;
    results[2] = y1_val;
    results[3] = y2_val;
}