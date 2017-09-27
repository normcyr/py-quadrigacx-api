import quadrigacx, check_profitability, send_email

quadrigacx.main()

eth_profit, btc_profit = check_profitability.main()

print(eth_profit)
print(btc_profit)

if eth_profit == True:
    send_email.main(eth_profit, btc_profit)
if btc_profit == True:
    send_email.main(btc_profit, btc_profit)
