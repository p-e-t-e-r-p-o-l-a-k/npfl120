paste en.tt te.tt | sed 's/\t/ ||| /' | grep '. ||| .' | grep -v '\. ||| \.'> en-te
./fast_align/build/fast_align -d -o -v -i en-te > en-te.f
./fast_align/build/fast_align -d -o -v -r -i en-te > en-te.r
./fast_align/build/atools -i en-te.f -j en-te.r -c intersect > en-te.i
./fast_align/build/atools -i en-te.f -j en-te.r -c union > en-te.u
