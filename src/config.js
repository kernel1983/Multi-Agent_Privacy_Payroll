require("dotenv").config();

const config = {
  // Kite AI支付配置
  kite: {
    rpcUrl: process.env.KITE_RPC_URL || "https://rpc-testnet.gokite.ai/",
    bundlerRpc:
      process.env.KITE_BUNDLER_RPC ||
      "https://bundler-service.staging.gokite.ai/rpc/",
    chainId: process.env.KITE_CHAIN_ID || 2368, // 默认KiteAI Testnet
  },

  // Agent配置
  agents: {
    hr: {
      privateKey: process.env.HR_AGENT_KEY || "",
    },
    payroll: {
      privateKey: process.env.PAYROLL_AGENT_KEY || "",
    },
    employee: {
      privateKey: process.env.EMPLOYEE_AGENT_KEY || "",
    },
  },

  // 环境配置
  environment: process.env.ENVIRONMENT || "development",

  // 加密配置
  encryption: {
    algorithm: "aes-256-cbc",
    ivLength: 16,
  },
};

module.exports = config;
