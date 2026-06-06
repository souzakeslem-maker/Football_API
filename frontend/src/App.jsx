import { useState, useEffect } from 'react'

const API_URL = 'http://localhost:8003'

const LIGAS = [
  { codigo: 'PL', nome: 'Premier League' },
  { codigo: 'BSA', nome: 'Brasileirão' },
  { codigo: 'CL', nome: 'Champions League' },
  { codigo: 'SA', nome: 'Serie A' },
]

function App() {
  const [liga, setLiga] = useState('PL')
  const [aba, setAba] = useState('times')
  const [dados, setDados] = useState([])
  const [loading, setLoading] = useState(true)
  const [erro, setErro] = useState(null)

  useEffect(() => {
    setLoading(true)
    setErro(null)
    setDados([])

    const endpoints = {
      times: `${API_URL}/times/${liga}`,
      partidas: `${API_URL}/partidas/${liga}`,
      artilheiros: `${API_URL}/artilheiros/${liga}`,
    }

    fetch(endpoints[aba])
      .then(r => r.json())
      .then(res => {
        if (aba === 'times') setDados(res.times)
        if (aba === 'partidas') setDados(res.partidas)
        if (aba === 'artilheiros') setDados(res.artilheiros)
        setLoading(false)
      })
      .catch(err => {
        setErro(err.message)
        setLoading(false)
      })
  }, [liga, aba])

  const tableStyle = { width: '100%', borderCollapse: 'collapse' }
  const thStyle = { padding: '10px', background: '#007bff', color: '#fff', textAlign: 'center' }
  const tdStyle = { padding: '10px', borderBottom: '1px solid #eee', textAlign: 'center' }

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif', maxWidth: 800, margin: '0 auto' }}>
      <h1 style={{ textAlign: 'center' }}>⚽ Futebol API</h1>

      {/* Seletor de liga */}
      <div style={{ textAlign: 'center', marginBottom: '1rem' }}>
        <select value={liga} onChange={e => setLiga(e.target.value)} style={{ padding: 8, fontSize: 14 }}>
          {LIGAS.map(l => <option key={l.codigo} value={l.codigo}>{l.nome}</option>)}
        </select>
      </div>

      {/* Abas */}
      <div style={{ display: 'flex', justifyContent: 'center', gap: 8, marginBottom: '1.5rem' }}>
        {['times', 'partidas', 'artilheiros'].map(a => (
          <button
            key={a}
            onClick={() => setAba(a)}
            style={{
              padding: '8px 20px',
              background: aba === a ? '#007bff' : '#eee',
              color: aba === a ? '#fff' : '#333',
              border: 'none',
              borderRadius: 4,
              cursor: 'pointer',
              textTransform: 'capitalize',
              fontWeight: aba === a ? 'bold' : 'normal'
            }}
          >
            {a}
          </button>
        ))}
      </div>

      {loading && <p style={{ textAlign: 'center' }}>Carregando...</p>}
      {erro && <p style={{ color: 'red', textAlign: 'center' }}>Erro: {erro}</p>}

      {/* Times */}
      {!loading && !erro && aba === 'times' && (
        <table style={tableStyle}>
          <thead>
            <tr>
              <th style={thStyle}>Escudo</th>
              <th style={thStyle}>Nome</th>
              <th style={thStyle}>Estádio</th>
              <th style={thStyle}>Fundado</th>
            </tr>
          </thead>
          <tbody>
            {dados.map(time => (
              <tr key={time.id}>
                <td style={tdStyle}><img src={time.escudo} width={28} alt="" /></td>
                <td style={tdStyle}><strong>{time.nome}</strong></td>
                <td style={tdStyle}>{time.estadio ?? '-'}</td>
                <td style={tdStyle}>{time.fundado ?? '-'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {/* Partidas */}
      {!loading && !erro && aba === 'partidas' && (
        <table style={tableStyle}>
          <thead>
            <tr>
              <th style={thStyle}>Rodada</th>
              <th style={thStyle}>Casa</th>
              <th style={thStyle}>Placar</th>
              <th style={thStyle}>Fora</th>
              <th style={thStyle}>Status</th>
              <th style={thStyle}>Data</th>
            </tr>
          </thead>
          <tbody>
            {dados.map(p => (
              <tr key={p.id}>
                <td style={tdStyle}>{p.rodada}</td>
                <td style={tdStyle}><strong>{p.time_casa}</strong></td>
                <td style={tdStyle}>{p.placar_casa ?? '-'} x {p.placar_fora ?? '-'}</td>
                <td style={tdStyle}><strong>{p.time_fora}</strong></td>
                <td style={tdStyle}>{p.status}</td>
                <td style={tdStyle}>{new Date(p.data).toLocaleDateString('pt-BR')}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {/* Artilheiros */}
      {!loading && !erro && aba === 'artilheiros' && (
        <table style={tableStyle}>
          <thead>
            <tr>
              <th style={thStyle}>#</th>
              <th style={thStyle}>Jogador</th>
              <th style={thStyle}>Time</th>
              <th style={thStyle}>Gols</th>
              <th style={thStyle}>Assistências</th>
            </tr>
          </thead>
          <tbody>
            {dados.map(a => (
              <tr key={a.posicao}>
                <td style={tdStyle}>{a.posicao}</td>
                <td style={tdStyle}>{a.jogador}</td>
                <td style={tdStyle}>{a.time}</td>
                <td style={tdStyle}>{a.gols}</td>
                <td style={tdStyle}>{a.assistencias ?? '-'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}

export default App