@echo off
title Trabalho de Complexidade de Algoritmos - Menu Principal
color 0A

:menu
cls
echo ============================================================
echo    TRABALHO DE COMPLEXIDADE DE ALGORITMOS
echo    Algoritmo RecomendaFacil - Vassouras Tech
echo    Professor - Marcio Guarrido
echo    Aluno - Leandro Loffeu Pereira Costa - Mat. 202212089
echo ============================================================
echo.
echo Escolha uma opcao:
echo.
echo [1] Executar analise completa
echo [2] Ver informacoes do projeto
echo [3] Abrir grafico
echo [4] Ver arquivos disponiveis
echo [5] Sair
echo.
echo ============================================================
set /p opcao="Digite sua opcao (1-5): "

if "%opcao%"=="1" goto executar
if "%opcao%"=="2" goto info
if "%opcao%"=="3" goto grafico
if "%opcao%"=="4" goto arquivos
if "%opcao%"=="5" goto sair
goto invalida

:executar
cls
echo ============================================================
echo    EXECUTANDO ANALISE COMPLETA
echo ============================================================
echo.
python trabalho.py
echo.
echo ============================================================
echo Analise concluida!
echo ============================================================
pause
goto menu

:info
cls
echo ============================================================
echo    INFORMACOES DO PROJETO
echo ============================================================
echo.
echo Algoritmo: RecomendaFacil
echo Funcao: f(n) = 2n - 1
echo Complexidade: O(n) - Linear
echo Limite n10: 19 recomendacoes
echo.
echo Objetivos:
echo - Calcular limite da funcao quando n tende a 10
echo - Analisar complexidade assintotica O(n)
echo - Discutir escalabilidade do sistema
echo - Implementar algoritmo conforme especificacao
echo.
echo Arquivos:
echo - trabalho.py (codigo principal)
echo - grafico.png (grafico da funcao)
echo - README.md (documentacao)
echo - executar.bat (este menu)
echo.
pause
goto menu

:grafico
cls
echo ============================================================
echo    ABRINDO GRAFICO
echo ============================================================
echo.
if exist grafico.png (
    echo Abrindo grafico.png...
    start grafico.png
    echo Grafico aberto!
) else (
    echo Grafico nao encontrado!
    echo Execute a opcao 1 primeiro para gerar o grafico.
)
echo.
pause
goto menu

:arquivos
cls
echo ============================================================
echo    ARQUIVOS DISPONIVEIS
echo ============================================================
echo.
echo Verificando arquivos...
echo.
if exist trabalho.py (
    echo [OK] trabalho.py - Codigo principal
) else (
    echo [ERRO] trabalho.py - NAO ENCONTRADO
)
if exist grafico.png (
    echo [OK] grafico.png - Grafico da funcao
) else (
    echo [AVISO] grafico.png - Nao gerado ainda
)
if exist README.md (
    echo [OK] README.md - Documentacao
) else (
    echo [ERRO] README.md - NAO ENCONTRADO
)
if exist executar.bat (
    echo [OK] executar.bat - Menu principal
) else (
    echo [ERRO] executar.bat - NAO ENCONTRADO
)
echo.
echo Total de arquivos: 4
echo.
pause
goto menu

:invalida
cls
echo ============================================================
echo    OPCAO INVALIDA!
echo ============================================================
echo.
echo Por favor, escolha uma opcao entre 1 e 5.
echo.
pause
goto menu

:sair
cls
echo ============================================================
echo    OBRIGADO POR USAR O SISTEMA!
echo ============================================================
echo.
echo Trabalho de Complexidade de Algoritmos
echo Algoritmo RecomendaFacil - Vassouras Tech
echo.
echo Desenvolvido com carinho e muito amor para o meu professor preferido!
echo.
timeout /t 10 >nul
exit
