#!/bin/bash

OUTPUT="Final_RFP_${RANDOM}.txt"
> $OUTPUT

# Read variables from input
declare -A vars
while IFS='=' read -r key value; do
    if [[ $key =~ ^[[:space:]]*# ]] || [[ -z $key ]]; then continue; fi
    key=$(echo $key | xargs)
    value=$(echo $value | sed 's/^ *"//;s/" *$//')
    vars[$key]=$value
done < customer_inputs.txt

# Process modules
for module in modules/*/*.txt; do
    content=$(<"$module")
    for key in "${!vars[@]}"; do
        content=$(echo "$content" | sed "s|\${${key}}|${vars[$key]}|g")
    done
    echo "$content" >> $OUTPUT
    echo -e "
---
" >> $OUTPUT
done

echo "✅ RFP generated: $OUTPUT"