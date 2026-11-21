#!/usr/bin/env bash
# Timer do projeto Mansão Blackwood.
# Espera 40 minutos e reabre o Freebuff neste diretório, retomando a última conversa.
#
# Uso normal:  bash retomar.sh
# Em janela nova: cmd //c start "Freebuff - retomar" bash -lc "cd /c/Users/eduardo/Desktop/detetive && bash retomar.sh"
#
# Cancelar: feche a janela do timer, ou: kill "$(cat .freebuff/retomar.pid)"

set -u
cd "$(dirname "$0")" || exit 1
mkdir -p .freebuff
echo $$ > .freebuff/retomar.pid

echo "Timer iniciado às $(date '+%H:%M'). Freebuff abre às $(date -d '+40 minutes' '+%H:%M' 2>/dev/null || echo '~40 min')."
echo "PID $$ — cancele com: kill \$(cat .freebuff/retomar.pid)"

sleep 2400

echo "$(date '+%H:%M') — abrindo Freebuff (--continue) em $(pwd)"
exec freebuff --continue --cwd "$(pwd)"
