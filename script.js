import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 5,
  duration: '30s',
};

export default function () {
  const res = http.get('http://127.0.0.1:3000/api/data');
  check(res, {
    'status 200 байна': (r) => r.status === 200,
  });
  sleep(1);
}

