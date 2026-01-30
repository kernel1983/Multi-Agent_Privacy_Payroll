<template>
  <div class="dashboard">
    <h1>Agent 网络</h1>

    <div class="status-grid">
      <!-- 网络信息 -->
      <div class="status-card">
        <h3>网络信息</h3>
        <div class="status-item">
          <span class="label">网络：</span>
          <span class="value">Kite Testnet</span>
        </div>
        <div class="status-item">
          <span class="label">链 ID：</span>
          <span class="value">2368 (0x940)</span>
        </div>
      </div>

      <!-- Agent 地址 -->
      <div class="status-card">
        <h3>Agent 地址</h3>
        <div class="status-item">
          <span class="label">HR Agent：</span>
          <span class="value address"
            >0x0987654321098765432109876543210987654321</span
          >
        </div>
        <div class="status-item">
          <span class="label">Payroll Agent：</span>
          <span class="value address"
            >0x876aed9838F32075359d259dab4274F125D01359</span
          >
        </div>
        <div class="status-item">
          <span class="label">Employee Agent：</span>
          <span class="value address"
            >0x1122334455667788990011223344556677889900</span
          >
        </div>
      </div>

      <!-- 核心流程 -->
      <div class="status-card">
        <h3>核心支付流程</h3>
        <div class="status-item">
          <span class="label">流程：</span>
          <span class="value">HR Agent → Payroll Agent → Employee Agent</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// 简化版本，移除系统状态更新逻辑
</script>

<style scoped>
.dashboard {
  padding: 20px;
}

.status-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.status-card {
  background: #f5f5f5;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.status-card h3 {
  margin-top: 0;
  margin-bottom: 15px;
  color: #333;
  font-size: 16px;
  border-bottom: 1px solid #ddd;
  padding-bottom: 10px;
}

.status-item {
  margin-bottom: 10px;
  display: flex;
  flex-direction: column;
}

.label {
  font-size: 14px;
  color: #666;
  margin-bottom: 5px;
}

.value {
  font-size: 14px;
  color: #333;
  font-family: "Courier New", monospace;
}

.address {
  font-size: 12px;
  word-break: break-all;
}

.status-badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
}

.status-badge.success {
  background: #e6f7ee;
  color: #137333;
}

.status-badge.failed {
  background: #fff1f0;
  color: #c5221f;
}

.status-badge.pending {
  background: #fffbf0;
  color: #d48806;
}
</style>
