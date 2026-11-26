\\ Finite cross-check of the proved all-level genus formulas.
check(ok,msg)={if(!ok,error(msg));};
check(valuation(269^2-1,3)==3,"wrong lifting-exponent constant");
h=t-3*t^2+3*t^3-30;
r=polrootspadic(h,3,80)[1];
check(valuation((-1+3*r)^3-269,3)>=79,"three-adic root verification");
print("CUBE_ROOT_Q3_PRECISION=",padicprec((-1+3*r)^3-269,3));
for(n=0,10,my(f=znorder(Mod(269,3^(n+1))),count=eulerphi(3^(n+1))/f,v=valuation(269^f-1,3),unit_index=if(v>=n+2,1,3),dimension);dimension=count-1-valuation(unit_index,3);check(f==2*3^max(n-2,0),"wrong residue degree");check(count==3^min(n,2),"wrong prime count");check(dimension==if(n==0,0,if(n==1,2,7)),"wrong genus dimension");print([n,f,count,v,unit_index,dimension]));
print("GENUS_START_CHECK_COMPLETE");
quit
