langs="ar cs de en es fi fr hi it ja pt ru sv tr zh"

for src in $langs; do
    for tgt in $langs; do
        temp_file=$(mktemp)
        python3 project.py treeproj/PUD/${src}_pud-ud-test.conllu treeproj/PUD/${tgt}_pud-ud-test.conllu treeproj/align/${src}-${tgt}/${src}-${tgt}.union >${temp_file}
        head=`python3 treeproj/evaluator.py -j -m head treeproj/PUD/${tgt}_pud-ud-test.conllu ${temp_file}`
        deprel=`python3 treeproj/evaluator.py -j -m deprel treeproj/PUD/${tgt}_pud-ud-test.conllu ${temp_file}`
        las=`python3 treeproj/evaluator.py -j -m las treeproj/PUD/${tgt}_pud-ud-test.conllu ${temp_file}`
        rm ${temp_file}
        echo $src $tgt $head $deprel $las
    done
done